<script lang="ts">
	import { scaleBand, scaleOrdinal } from 'd3-scale';
	import { Axis, Bars, Chart, Frame, Grid, Highlight, isometric, Layer, Legend, Tooltip } from 'layerchart';
	import { SERIES, formatDay, formatDate, longRows, type ChartRow } from '#lib/stats.ts';

	let { rows }: { rows: ChartRow[] } = $props();

	const data = $derived(longRows(rows));
	const byKey = $derived(new Map(rows.map((r) => [r.key, r])));
	// Label every release until the dates would run into each other, then every second or third
	const ticks = $derived.by(() => {
		const step = Math.ceil(rows.length / 11);
		return rows.filter((_, i) => i % step === 0).map((r) => r.key);
	});
	const tick = (key: string) => {
		const row = byKey.get(key);
		return row ? formatDay(row.date) : key;
	};
</script>

<!-- Releases across the floor in one row, with each release's change types stacked up along `z`.
     Solid colours, since translucent boxes would show their insides -->
<div class="h-[460px]">
	<Chart
		{data}
		x="key"
		xScale={scaleBand().paddingInner(0.45).paddingOuter(0.2)}
		xDomain={rows.map((r) => r.key)}
		y="row"
		yScale={scaleBand().padding(0.25)}
		z="value"
		zNice
		valueAxis="z"
		zRange={({ width }: { width: number }) => [0, width * 0.42]}
		c="series"
		cScale={scaleOrdinal()}
		cDomain={SERIES.map((s) => s.label)}
		cRange={SERIES.map((s) => s.color)}
		view={isometric({ rotate: -22, tilt: 68, aspect: Math.max(4, rows.length * 0.7) })}
		transform={{ mode: 'canvas', drag: 'rotate' }}
		tooltipContext={{ mode: 'manual' }}
		padding={{ top: 16, bottom: 64, left: 24, right: 24 }}
		clip
	>
		<Layer>
			<Frame class="fill-ink/4 stroke-ink/20" />
			<Grid z />
			<Axis placement="bottom" format={tick} {ticks} tickLabelProps={{ viewport: true }} />
			<Axis placement="back" format="integer" />
			<!-- Each box is its own hit area, as the floor cell under the pointer may be another box -->
			<Bars tooltip strokeWidth={1} stroke="var(--surface-1)" />
			<Highlight points={{ r: 4 }} />
		</Layer>

		<Legend placement="bottom" variant="swatches" />

		<Tooltip.Root>
			{#snippet children({ data })}
				<Tooltip.Header>{data.label} · {formatDate(data.date)}</Tooltip.Header>
				<Tooltip.List>
					<Tooltip.Item label={data.series} value={data.value} color={data.color} format="integer" />
					<Tooltip.Separator />
					<Tooltip.Item label="release total" value={byKey.get(data.key)?.total} format="integer" />
				</Tooltip.List>
			{/snippet}
		</Tooltip.Root>
	</Chart>
</div>
