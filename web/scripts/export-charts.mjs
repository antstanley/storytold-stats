// Export every chart on every repo page as a PNG, for the reports in ../reports.
//   node scripts/export-charts.mjs [baseUrl] [light|dark|both] [outDir]
// Writes <outDir>/<theme>/<repo>-<chart>.png, where <chart> is the card's data-chart name
// (changes-line, changes-bar, contributors, agent-disclosure).
// Needs the app running (pnpm dev / pnpm preview) and a local Google Chrome.
import { chromium } from 'playwright-core';
import { mkdir, readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

const [baseUrl = 'http://localhost:5173', theme = 'both', outArg] = process.argv.slice(2);
const outDir = outArg ?? fileURLToPath(new URL('../../charts', import.meta.url));
const themes = theme === 'both' ? ['light', 'dark'] : [theme];
const stats = JSON.parse(await readFile(new URL('../src/lib/data/stats.json', import.meta.url), 'utf8'));

const browser = await chromium.launch({ channel: 'chrome' });
let written = 0;
for (const scheme of themes) {
	await mkdir(`${outDir}/${scheme}`, { recursive: true });
	const page = await browser.newPage({
		viewport: { width: 1200, height: 1000 },
		deviceScaleFactor: 2,
		colorScheme: scheme
	});
	for (const { name } of stats.repos) {
		await page.goto(`${baseUrl}/${name}`, { waitUntil: 'networkidle' });
		for (const card of await page.locator('section[data-chart]').all()) {
			const chart = await card.getAttribute('data-chart');
			await card.scrollIntoViewIfNeeded();
			// Bars or release points: whichever this chart draws last
			// (attached, not visible: the first bar can be a zero-height one)
			await card
				.locator('.lc-root-container svg :is(circle, .lc-bar)')
				.first()
				.waitFor({ state: 'attached' });
			// The card's heading doesn't say which repo it is; an exported image has to
			await card
				.locator('h2')
				.evaluate((h2, repo) => (h2.textContent = `${repo}: ${h2.textContent.toLowerCase()}`), name);
			await page.mouse.move(0, 0);
			await card.screenshot({ path: `${outDir}/${scheme}/${name}-${chart}.png` });
			written++;
		}
	}
	await page.close();
}
await browser.close();
console.log(`${written} charts written to ${outDir}`);
