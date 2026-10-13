<script lang="ts">
	import { AreaChart } from 'layerchart';
	import { scaleUtc } from 'd3-scale';
	import { SERIES, formatDate, type ChartRow } from '#lib/stats.ts';
	import { timeAxis } from '#lib/time-axis.ts';

	let { rows }: { rows: ChartRow[] } = $props();

	const series = SERIES.map(({ key, label, color }) => ({ key, label, color }));
	const byTime = $derived(new Map(rows.map((r) => [r.date.getTime(), r])));

	const axis = $derived(timeAxis(rows.map((r) => r.date)));

	function header(value: Date) {
		const row = byTime.get(value.getTime());
		return row ? `${row.label} · ${formatDate(value)}` : formatDate(value);
	}
</script>

<div class="h-[380px]">
	<AreaChart
		data={rows}
		x="date"
		xScale={scaleUtc()}
		{series}
		seriesLayout="stack"
		legend
		points={{ r: 3 }}
		padding={{ top: 12, right: 16, bottom: 56, left: 36 }}
		props={{
			area: { fillOpacity: 0.25, line: { strokeWidth: 2 } },
			xAxis: { format: axis.format, ticks: axis.ticks },
			yAxis: { format: 'integer' },
			tooltip: { header: { format: header } }
		}}
	/>
</div>
