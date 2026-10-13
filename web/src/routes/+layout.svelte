<script lang="ts">
	import './layout.css';
	import favicon from '#lib/assets/favicon.svg';
	import { page } from '$app/state';
	import { resolve } from '$app/paths';
	import { repos, generated } from '#lib/stats.ts';
	import type { LayoutProps } from './$types';

	let { children }: LayoutProps = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="mx-auto max-w-6xl px-4 py-6 sm:px-6">
	<header class="mb-6">
		<a href={resolve('/')} class="text-lg font-semibold text-ink">storytold — changes per release</a>
		<nav class="mt-3 flex flex-wrap gap-1.5" aria-label="Repositories">
			{#each repos as repo (repo.name)}
				{@const current = page.params.repo === repo.name}
				<a
					href={resolve('/[repo]', { repo: repo.name })}
					aria-current={current ? 'page' : undefined}
					class={[
						'rounded-full border px-3 py-1 text-sm',
						current
							? 'border-ink bg-ink text-surface'
							: 'border-hairline bg-surface text-ink-2 hover:text-ink'
					]}
				>
					{repo.name}
				</a>
			{/each}
		</nav>
	</header>

	{@render children()}

	<footer class="mt-10 border-t border-hairline pt-4 text-sm text-muted">
		Data generated {generated} from github.com/storytold. Counts are changes (PR merges, squash
		merges, direct commits), not lines of code.
	</footer>
</div>
