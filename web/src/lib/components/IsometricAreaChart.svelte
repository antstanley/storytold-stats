<script lang="ts">
	import { scaleBand, scaleOrdinal, scaleUtc } from 'd3-scale';
	import { Area, Axis, Chart, Frame, Grid, Highlight, isometric, Layer, Legend, Tooltip } from 'layerchart';
	import { SERIES, formatDate, longRows, type ChartRow } from '#lib/stats.ts';
	import { timeAxis } from '#lib/time-axis.ts';

	let { rows }: { rows: ChartRow[] } = $props();

	// Every release for every series, zeros included, so each curtain runs the whole floor
	const data = $derived(longRows(rows, { zeros: true }));
	const axis = $derived(timeAxis(rows.map((r) => r.date)));
	const names = SERIES.map((s) => s.label);
</script>

<!-- Each change type a curtain standing in its own row, as tall as its count at each release -->
<div class="h-[460px]">
	<Chart
		{data}
		x="date"
		xScale={scaleUtc()}
		y="series"
		yScale={scaleBand().paddingInner(0.4)}
		yDomain={names}
		z="value"
		zNice
		zRange={({ width }: { width: number }) => [0, width * 0.3]}
		c="series"
		cScale={scaleOrdinal()}
		cDomain={names}
		cRange={SERIES.map((s) => s.color)}
		view={isometric({ rotate: -40, tilt: 65, aspect: 2.2 })}
		transform={{ mode: 'canvas', drag: 'rotate' }}
		tooltipContext={{ mode: 'quadtree' }}
		padding={{ top: 16, bottom: 64, left: 24, right: 24 }}
		clip
	>
		{#snippet children({ context })}
			{@const m = context.isometricMatrix}
			<Layer>
				<Frame class="fill-ink/4 stroke-ink/20" />
				<Grid x z />
				<Axis
					placement="bottom"
					format={axis.format}
					ticks={axis.ticks}
					tickLabelProps={{ viewport: true }}
				/>
				<Axis placement="left" tickLabelProps={{ viewport: true }} />
				<Axis placement="back" format="integer" />

				<!-- Back to front: each curtain lies in its own row, so the farther rows go first -->
				{#each [...SERIES].sort( (a, b) => (m ? m.d * (context.yScale(a.label) - context.yScale(b.label)) : 0) ) as s (s.key)}
					<Area
						data={data.filter((d) => d.series === s.label)}
						fill={s.color}
						fillOpacity={0.75}
						line={{ stroke: s.color, strokeWidth: 2 }}
					/>
				{/each}
				<Highlight points={{ r: 4 }} />
			</Layer>

			<Legend placement="bottom" variant="swatches" />

			<Tooltip.Root>
				{#snippet children({ data })}
					<Tooltip.Header>{data.label} · {formatDate(data.date)}</Tooltip.Header>
					<Tooltip.List>
						<Tooltip.Item label={data.series} value={data.value} color={data.color} format="integer" />
					</Tooltip.List>
				{/snippet}
			</Tooltip.Root>
		{/snippet}
	</Chart>
</div>
