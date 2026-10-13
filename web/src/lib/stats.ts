import raw from './data/stats.json';

export const CATEGORIES = [
	'feature',
	'fix',
	'perf',
	'i18n',
	'docs',
	'test',
	'build-ci',
	'release',
	'refactor',
	'deps',
	'security',
	'revert',
	'other'
] as const;
export type Category = (typeof CATEGORIES)[number];

export const CATEGORY_LABELS: Record<Category, string> = {
	feature: 'Feature',
	fix: 'Fix',
	perf: 'Perf',
	i18n: 'i18n',
	docs: 'Docs',
	test: 'Test',
	'build-ci': 'Build/CI',
	release: 'Release',
	refactor: 'Refactor',
	deps: 'Deps',
	security: 'Security',
	revert: 'Revert',
	other: 'Other'
};

/**
 * Chart series. Eight is the most a categorical palette can keep distinguishable, so the six
 * small housekeeping categories are drawn as one "Maintenance & other" series. The table under
 * the charts keeps all thirteen.
 */
export const SERIES = [
	{ key: 'feature', label: 'Feature', color: 'var(--series-1)', categories: ['feature'] },
	{ key: 'fix', label: 'Fix', color: 'var(--series-2)', categories: ['fix'] },
	{ key: 'perf', label: 'Perf', color: 'var(--series-3)', categories: ['perf'] },
	{ key: 'i18n', label: 'i18n', color: 'var(--series-4)', categories: ['i18n'] },
	{ key: 'docs', label: 'Docs', color: 'var(--series-5)', categories: ['docs'] },
	{ key: 'test', label: 'Test', color: 'var(--series-6)', categories: ['test'] },
	{ key: 'buildci', label: 'Build/CI', color: 'var(--series-7)', categories: ['build-ci'] },
	{
		key: 'maintenance',
		label: 'Maintenance & other',
		color: 'var(--series-8)',
		categories: ['release', 'refactor', 'deps', 'security', 'revert', 'other']
	}
] as const satisfies readonly {
	key: string;
	label: string;
	color: string;
	categories: readonly Category[];
}[];
export type SeriesKey = (typeof SERIES)[number]['key'];

export type Release = {
	key: string;
	label: string;
	tags: string[];
	date: string;
	url: string;
	unreleased: boolean;
	uncategorised: boolean;
	commits: number;
	changes: number;
	counts: Record<Category, number>;
};
export type Repo = { name: string; releases: Release[] };

export const generated: string = raw.generated;
export const repos: Repo[] = raw.repos;

export function getRepo(name: string): Repo | undefined {
	return repos.find((r) => r.name === name);
}

/** One chart row per release: its date plus a count for each series. */
export type ChartRow = { key: string; label: string; date: Date; total: number } & Record<
	SeriesKey,
	number
>;

export function chartRows(releases: Release[]): ChartRow[] {
	return releases.map((r) => {
		const row = { key: r.key, label: r.label, date: new Date(r.date), total: r.changes } as ChartRow;
		for (const s of SERIES) {
			row[s.key] = s.categories.reduce((n: number, c: Category) => n + r.counts[c], 0);
		}
		return row;
	});
}

/** One row per release and series, for charts that take long data. Empty counts are left out. */
export type LongRow = {
	key: string;
	label: string;
	date: Date;
	series: string;
	color: string;
	value: number;
	/** The single row the stacked columns stand in */
	row: string;
};

export function longRows(rows: ChartRow[], { zeros = false } = {}): LongRow[] {
	return rows.flatMap((r) =>
		SERIES.filter((s) => zeros || r[s.key] > 0).map((s) => ({
			key: r.key,
			label: r.label,
			date: r.date,
			series: s.label,
			color: s.color,
			value: r[s.key],
			row: 'Changes'
		}))
	);
}

/** Sum of each category over released, categorised releases. */
export function totals(repo: Repo) {
	const counted = repo.releases.filter((r) => !r.unreleased && !r.uncategorised);
	const counts = Object.fromEntries(CATEGORIES.map((c) => [c, 0])) as Record<Category, number>;
	for (const r of counted) for (const c of CATEGORIES) counts[c] += r.counts[c];
	const released = repo.releases.filter((r) => !r.unreleased);
	return {
		releases: released.length,
		changes: counted.reduce((n, r) => n + r.changes, 0),
		counts,
		first: released[0]?.date,
		last: released.at(-1)?.date
	};
}

const dayMonth = new Intl.DateTimeFormat('en-GB', { day: 'numeric', month: 'short', timeZone: 'UTC' });
const month = new Intl.DateTimeFormat('en-GB', { month: 'short', timeZone: 'UTC' });
const monthYear = new Intl.DateTimeFormat('en-GB', { month: 'short', year: '2-digit', timeZone: 'UTC' });
const dayMonthYear = new Intl.DateTimeFormat('en-GB', {
	day: 'numeric',
	month: 'short',
	year: 'numeric',
	timeZone: 'UTC'
});

/** Month tick; January carries the year so a new year is visible on the axis. */
export const formatMonth = (d: Date | string) => {
	const date = new Date(d);
	return (date.getUTCMonth() === 0 ? monthYear : month).format(date);
};
/** Time of day, UTC, for axes that span only a few days. */
export const formatTime = (d: Date | string) => new Date(d).toISOString().slice(11, 16);
export const formatDay = (d: Date | string) => dayMonth.format(new Date(d));
export const formatDate = (d: Date | string) => dayMonthYear.format(new Date(d));
export const formatCount = (n: number) => n.toLocaleString('en-GB');
