# storytold release charts

SvelteKit + [LayerChart](https://layerchart.com) charts of the per-release change stats in `../csv/release_stats.csv`.

For every repo there is a page with two charts, both with the release date on the x-axis, the number of changes on the y-axis and one series per change type:

- a stacked line (area) chart
- a stacked bar chart, one bar per release

A Flat / Isometric toggle on each repo page swaps both charts for LayerChart's isometric view: a curtain per change type for the line chart, and stacked 3D columns for the bar chart. Drag either one to rotate it.

```sh
pnpm install
pnpm dev        # http://localhost:5173
pnpm build      # static site in build/
```

## Data

`src/lib/data/stats.json` is generated; refresh it after re-running the stats pipeline:

```sh
python3 ../scripts/export_web.py
```

## Where things are

- `src/lib/stats.ts` — data types, the eight chart series and which categories each one covers
- `src/lib/components/StackedLineChart.svelte`, `StackedBarChart.svelte` — the two flat charts
- `src/lib/components/IsometricAreaChart.svelte`, `IsometricColumnChart.svelte` — their isometric versions
- `scripts/export-charts.mjs` — exports each repo's stacked line chart as a PNG
- `src/routes/[repo]/+page.svelte` — a repo's page (charts plus a table with all thirteen categories)
- `src/routes/layout.css` — colours for light and dark mode
