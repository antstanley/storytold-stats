<script lang="ts">
	import StackedLineChart from '#lib/components/StackedLineChart.svelte';
	import StackedBarChart from '#lib/components/StackedBarChart.svelte';
	import IsometricAreaChart from '#lib/components/IsometricAreaChart.svelte';
	import IsometricColumnChart from '#lib/components/IsometricColumnChart.svelte';
	import { view } from '#lib/view.svelte.ts';
	import {
		CATEGORIES,
		CATEGORY_LABELS,
		CONTRIBUTOR_SERIES,
		DISCLOSURE_SERIES,
		SERIES,
		chartRows,
		contributorRows,
		disclosureRows,
		totals,
		formatDate,
		formatCount
	} from '#lib/stats.ts';
	import type { PageProps } from './$types';

	let { data }: PageProps = $props();

	let includeUnreleased = $state(false);

	const repo = $derived(data.repo);
	const sum = $derived(totals(repo));
	const unreleased = $derived(repo.releases.find((r) => r.unreleased));
	const rows = $derived(
		chartRows(
			repo.releases.filter((r) => includeUnreleased || !r.unreleased)
		)
	);

	const charted = $derived(
		repo.releases.filter((r) => includeUnreleased || !r.unreleased)
	);
	const peopleRows = $derived(contributorRows(charted));
	const agentRows = $derived(disclosureRows(charted));

	const disclosed = $derived(
		repo.releases
			.filter((r) => !r.unreleased)
			.reduce((n, r) => n + r.contributors.agentDisclosed, 0)
	);
	// A handful out of thousands is not 0%
	function share(part: number, whole: number) {
		if (!whole) return '–';
		const pct = (100 * part) / whole;
		return part > 0 && pct < 1 ? '<1%' : `${Math.round(pct)}%`;
	}
	const changes = (n: number) => `${formatCount(n)} ${n === 1 ? 'change' : 'changes'}`;
	const peopleTiles = $derived([
		{ label: 'Humans', value: formatCount(repo.people.humans) },
		{ label: 'Agents disclosed', value: formatCount(repo.people.agents.length) },
		{ label: 'Bots', value: formatCount(repo.people.bots) },
		{ label: 'Changes disclosing an agent', value: formatCount(disclosed) },
		{
			label: 'Share of changes',
			value: share(disclosed, sum.changes)
		}
	]);

	const tiles = $derived([
		{ label: 'Releases', value: sum.releases },
		{ label: 'Changes', value: sum.changes },
		{ label: 'Features', value: sum.counts.feature },
		{ label: 'Fixes', value: sum.counts.fix },
		{ label: 'Perf', value: sum.counts.perf }
	]);
</script>

<svelte:head>
	<title>{repo.name} — changes per release</title>
</svelte:head>

<h1 class="text-2xl font-semibold">{repo.name}</h1>
<p class="mt-1 text-sm text-ink-2">
	{sum.releases} releases, {sum.first ? formatDate(sum.first) : ''} to {sum.last
		? formatDate(sum.last)
		: ''}. Each point is one release; its value is the number of changes that landed since the
	previous release.
</p>

<dl class="mt-5 grid grid-cols-2 gap-3 sm:grid-cols-5">
	{#each tiles as tile (tile.label)}
		<div class="rounded-lg border border-hairline bg-surface px-4 py-3">
			<dt class="text-sm text-ink-2">{tile.label}</dt>
			<dd class="mt-0.5 text-2xl font-semibold">{formatCount(tile.value)}</dd>
		</div>
	{/each}
</dl>

<div class="mt-5 flex flex-wrap items-center gap-x-6 gap-y-3">
	<div class="flex rounded-lg border border-hairline bg-surface p-0.5 text-sm" role="group" aria-label="Chart view">
		{#each [{ label: 'Flat', value: false }, { label: 'Isometric', value: true }] as option (option.label)}
			<button
				type="button"
				aria-pressed={view.isometric === option.value}
				onclick={() => (view.isometric = option.value)}
				class={[
					'rounded-md px-3 py-1',
					view.isometric === option.value ? 'bg-ink text-surface' : 'text-ink-2 hover:text-ink'
				]}
			>
				{option.label}
			</button>
		{/each}
	</div>

	{#if unreleased}
		<label class="flex w-fit items-center gap-2 text-sm text-ink-2">
			<input type="checkbox" bind:checked={includeUnreleased} class="size-4 accent-(--series-1)" />
			Include the {formatCount(unreleased.changes)} unreleased changes on main
		</label>
	{/if}
</div>

<section data-chart="changes-line" class="mt-4 rounded-lg border border-hairline bg-surface p-4">
	{#if view.isometric}
		<h2 class="font-semibold">Changes per release, one curtain per type</h2>
		<p class="text-sm text-ink-2">
			Each type stands in its own row; height is its count in that release. Drag to rotate.
		</p>
		<div class="mt-3">
			<IsometricAreaChart {rows} series={SERIES} />
		</div>
	{:else}
		<h2 class="font-semibold">Changes per release, stacked by type</h2>
		<p class="text-sm text-ink-2">Stacked lines: the top line is the release's total.</p>
		<div class="mt-3">
			<StackedLineChart {rows} series={SERIES} />
		</div>
	{/if}
</section>

<section data-chart="changes-bar" class="mt-4 rounded-lg border border-hairline bg-surface p-4">
	<h2 class="font-semibold">Changes per release, by type</h2>
	{#if view.isometric}
		<p class="text-sm text-ink-2">
			One stacked column per release, labelled with its release date. Drag to rotate.
		</p>
		<div class="mt-3">
			<IsometricColumnChart {rows} series={SERIES} />
		</div>
	{:else}
		<p class="text-sm text-ink-2">One bar per release, labelled with its release date.</p>
		<div class="mt-3">
			<StackedBarChart {rows} series={SERIES} />
		</div>
	{/if}
</section>

<h2 class="mt-10 text-xl font-semibold">Contributors</h2>
<p class="mt-1 text-sm text-ink-2">
	Who the released changes came from. An agent counts as disclosed when it is a commit's git author,
	is named in a Co-authored-by trailer, or the message says it was generated with one, so these
	figures are a floor.
</p>

<dl class="mt-4 grid grid-cols-2 gap-3 sm:grid-cols-5">
	{#each peopleTiles as tile (tile.label)}
		<div class="rounded-lg border border-hairline bg-surface px-4 py-3">
			<dt class="text-sm text-ink-2">{tile.label}</dt>
			<dd class="mt-0.5 text-2xl font-semibold">{tile.value}</dd>
		</div>
	{/each}
</dl>

<section data-chart="contributors" class="mt-4 rounded-lg border border-hairline bg-surface p-4">
	<h2 class="font-semibold">Unique contributors per release</h2>
	<p class="text-sm text-ink-2">
		Humans who appear in a release for the first time are new; agents are counted by product, so
		every Claude model is one agent.{view.isometric ? ' Drag to rotate.' : ''}
	</p>
	<div class="mt-3">
		{#if view.isometric}
			<IsometricColumnChart rows={peopleRows} series={CONTRIBUTOR_SERIES} />
		{:else}
			<StackedBarChart rows={peopleRows} series={CONTRIBUTOR_SERIES} />
		{/if}
	</div>
</section>

<section data-chart="agent-disclosure" class="mt-4 rounded-lg border border-hairline bg-surface p-4">
	<h2 class="font-semibold">Changes per release, by agent disclosure</h2>
	<p class="text-sm text-ink-2">
		{#if view.isometric}
			One curtain per kind of change; height is its count in that release. Drag to rotate.
		{:else}
			Stacked lines: the top line is the release's total.
		{/if}
	</p>
	<div class="mt-3">
		{#if view.isometric}
			<IsometricAreaChart rows={agentRows} series={DISCLOSURE_SERIES} />
		{:else}
			<StackedLineChart rows={agentRows} series={DISCLOSURE_SERIES} />
		{/if}
	</div>
</section>

<section class="mt-4 grid gap-4 sm:grid-cols-2">
	<div class="rounded-lg border border-hairline bg-surface p-4">
		<h2 class="font-semibold">Agents disclosed</h2>
		{#if repo.people.agents.length}
			<table class="mt-2 w-full text-sm tabular-nums">
				<tbody>
					{#each repo.people.agents as agent (agent.name)}
						<tr class="border-b border-gridline last:border-0">
							<td class="py-1.5">{agent.name}</td>
							<td class="py-1.5 text-right">{changes(agent.changes)}</td>
						</tr>
					{/each}
				</tbody>
			</table>
		{:else}
			<p class="mt-2 text-sm text-ink-2">No change in a release of this repo discloses an agent.</p>
		{/if}
	</div>
	<div class="rounded-lg border border-hairline bg-surface p-4">
		<h2 class="font-semibold">Most active humans</h2>
		<table class="mt-2 w-full text-sm tabular-nums">
			<tbody>
				{#each repo.people.top as person (person.name)}
					<tr class="border-b border-gridline last:border-0">
						<td class="py-1.5">{person.name}</td>
						<td class="py-1.5 text-right">{changes(person.changes)}</td>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
</section>

<h2 class="mt-10 text-xl font-semibold">Per-release table</h2>

<section class="mt-4 rounded-lg border border-hairline bg-surface p-4">
	<h2 class="font-semibold">All categories</h2>
	<p class="text-sm text-ink-2">
		The charts draw Release, Refactor, Deps, Security, Revert and Other as one “Maintenance &
		other” series; the table keeps them apart.
	</p>
	<div class="mt-3 overflow-x-auto">
		<table class="w-full text-sm tabular-nums">
			<thead>
				<tr class="border-b border-baseline text-right text-ink-2">
					<th class="py-1.5 pr-3 text-left font-medium">Release</th>
					<th class="px-2 text-left font-medium">Published</th>
					<th class="px-2 font-medium">Changes</th>
					{#each CATEGORIES as c (c)}
						<th class="px-2 font-medium">{CATEGORY_LABELS[c]}</th>
					{/each}
				</tr>
			</thead>
			<tbody>
				{#each repo.releases as r (r.key)}
					<tr class="border-b border-gridline text-right">
						<td class="py-1.5 pr-3 text-left whitespace-nowrap">
							{#if r.url}
								<a href={r.url} class="underline decoration-baseline underline-offset-2">{r.label}</a>
							{:else}
								<span class="text-ink-2">{r.label} (main)</span>
							{/if}
						</td>
						<td class="px-2 text-left whitespace-nowrap text-ink-2">{formatDate(r.date)}</td>
						<td class="px-2 font-medium">{formatCount(r.changes)}</td>
						{#each CATEGORIES as c (c)}
							<td class="px-2 {r.counts[c] ? '' : 'text-muted'}">
								{r.counts[c] || '·'}
							</td>
						{/each}
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
</section>
