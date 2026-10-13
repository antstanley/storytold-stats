// Export every repo's stacked line chart as a PNG.
//   node scripts/export-charts.mjs [baseUrl] [light|dark] [outDir]
// Needs the app running (pnpm dev / pnpm preview) and a local Google Chrome.
import { chromium } from 'playwright-core';
import { mkdir, readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

const [baseUrl = 'http://localhost:5173', scheme = 'dark', outArg] = process.argv.slice(2);
const outDir = outArg ?? fileURLToPath(new URL(`../../charts/${scheme}`, import.meta.url));
const stats = JSON.parse(await readFile(new URL('../src/lib/data/stats.json', import.meta.url), 'utf8'));

await mkdir(outDir, { recursive: true });
const browser = await chromium.launch({ channel: 'chrome' });
const page = await browser.newPage({
	viewport: { width: 1200, height: 1000 },
	deviceScaleFactor: 2,
	colorScheme: scheme
});

for (const { name } of stats.repos) {
	await page.goto(`${baseUrl}/${name}`, { waitUntil: 'networkidle' });
	const card = page.locator('section', { has: page.locator('.lc-root-container') }).first();
	// The release points are the last marks drawn
	await card.locator('.lc-root-container svg circle').first().waitFor();
	// The card's heading doesn't say which repo it is; an exported image has to
	await card.locator('h2').evaluate((h2, repo) => (h2.textContent = `${repo}: ${h2.textContent.toLowerCase()}`), name);
	await page.mouse.move(0, 0);
	const path = `${outDir}/${name}-stacked-line.png`;
	await card.screenshot({ path });
	console.log(path);
}
await browser.close();
