import { formatDay, formatMonth, formatTime } from './stats.ts';

const HOUR = 60 * 60 * 1000;
const DAY = 24 * HOUR;

/**
 * Ticks and tick labels for a UTC time axis over `dates` (ascending).
 *
 * Month ticks once the range runs to months, day ticks for a few weeks of releases, and
 * six-hourly ticks when every release fell within a few days. Explicit, because the default
 * picks sub-day ticks for a short range and a day label would then repeat.
 */
export function timeAxis(dates: Date[]): { ticks?: Date[]; format: (d: Date) => string } {
	if (!dates.length) return { format: formatDay };
	const start = dates[0].getTime();
	const end = dates.at(-1)!.getTime();
	const span = end - start;
	if (span > 60 * DAY) return { format: formatMonth };

	const every = span > 3 * DAY ? DAY : 6 * HOUR;
	const all: Date[] = [];
	for (let t = Math.ceil(start / every) * every; t <= end; t += every) all.push(new Date(t));
	const step = Math.ceil(all.length / 12);
	const ticks = all.filter((_, i) => i % step === 0);
	const first = ticks[0]?.getTime();

	return {
		ticks,
		format: (d) => {
			if (d.getTime() % DAY === 0) return formatDay(d);
			// The first tick names its day, or an axis that starts mid-day never says which day
			return d.getTime() === first ? `${formatDay(d)} ${formatTime(d)}` : formatTime(d);
		}
	};
}
