<script lang="ts">
	import { BarChart } from 'layerchart';
	import { formatDay, formatDate, type ChartRow, type SeriesDef } from '#lib/stats.ts';

	let { rows, series: defs }: { rows: ChartRow[]; series: readonly SeriesDef[] } = $props();

	const series = $derived(defs.map(({ key, label, color }) => ({ key, label, color })));
	const byKey = $derived(new Map(rows.map((r) => [r.key, r])));

	// Keep bars thin: widen the gaps instead of letting a few bars fill the plot
	const MAX_BAR = 28;
	let width = $state(0);
	const bandPadding = $derived.by(() => {
		const step = width > 0 && rows.length > 0 ? (width - 60) / rows.length : 0;
		return step > 0 ? Math.min(0.9, Math.max(0.25, 1 - MAX_BAR / step)) : 0.4;
	});
	const crowded = $derived(width > 0 && rows.length * 52 > width);

	const tick = (key: string) => {
		const row = byKey.get(key);
		return row ? formatDay(row.date) : key;
	};
	const header = (key: string) => {
		const row = byKey.get(key);
		return row ? `${row.label} · ${formatDate(row.date)}` : key;
	};
</script>

<div class="h-[380px]" bind:clientWidth={width}>
	<BarChart
		data={rows}
		x="key"
		{series}
		seriesLayout="stack"
		legend
		{bandPadding}
		padding={{ top: 12, right: 16, bottom: crowded ? 76 : 56, left: 36 }}
		props={{
			xAxis: {
				format: tick,
				tickLabelProps: crowded ? { rotate: 315, textAnchor: 'end' } : undefined
			},
			yAxis: { format: 'integer' },
			// A surface-coloured stroke is the 2px gap between segments. (stackPadding would do it
			// too, but it turns segments smaller than the gap into negative-height rects.)
			bars: { stroke: 'var(--surface-1)', strokeWidth: 2 },
			tooltip: { header: { format: header } }
		}}
	/>
</div>
