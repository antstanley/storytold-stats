<script lang="ts">
	import { resolve } from '$app/paths';
	import { repos, totals, SERIES, formatDate, formatCount } from '#lib/stats.ts';

	const cards = repos.map((repo) => {
		const sum = totals(repo);
		const parts = SERIES.map((s) => ({
			...s,
			value: s.categories.reduce((n: number, c) => n + sum.counts[c], 0)
		})).filter((p) => p.value > 0);
		return { repo, sum, parts };
	});
</script>

<svelte:head>
	<title>storytold — changes per release</title>
</svelte:head>

<h1 class="text-2xl font-semibold">Repositories</h1>
<p class="mt-1 text-sm text-ink-2">
	Pick a repository to see its changes per release as stacked line and bar charts.
</p>

<ul class="mt-3 flex flex-wrap gap-x-4 gap-y-1 text-sm text-ink-2" aria-label="Legend">
	{#each SERIES as s (s.key)}
		<li class="flex items-center gap-1.5">
			<span class="size-2.5 rounded-xs" style:background={s.color}></span>{s.label}
		</li>
	{/each}
</ul>

<ul class="mt-4 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
	{#each cards as { repo, sum, parts } (repo.name)}
		<li>
			<a
				href={resolve('/[repo]', { repo: repo.name })}
				class="block rounded-lg border border-hairline bg-surface p-4 hover:border-baseline"
			>
				<div class="flex items-baseline justify-between gap-2">
					<span class="font-semibold">{repo.name}</span>
					<span class="text-sm text-ink-2">{sum.releases} releases</span>
				</div>
				<div class="mt-1 text-sm text-ink-2">
					{sum.first ? formatDate(sum.first) : ''} – {sum.last ? formatDate(sum.last) : ''}
				</div>
				<div class="mt-3 text-2xl font-semibold">
					{formatCount(sum.changes)} <span class="text-sm font-normal text-ink-2">changes</span>
				</div>
				<div class="mt-2 flex h-2 gap-0.5" aria-hidden="true">
					{#each parts as p (p.key)}
						<span class="rounded-xs" style:background={p.color} style:flex-grow={p.value}></span>
					{/each}
				</div>
				<div class="mt-2 text-sm text-ink-2">
					{formatCount(sum.counts.feature)} features · {formatCount(sum.counts.fix)} fixes ·
					{formatCount(sum.counts.perf)} perf
				</div>
			</a>
		</li>
	{/each}
</ul>
