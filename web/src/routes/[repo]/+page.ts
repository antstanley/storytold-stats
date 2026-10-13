import { error } from '@sveltejs/kit';
import { getRepo, repos } from '#lib/stats.ts';
import type { EntryGenerator, PageLoad } from './$types';

export const entries: EntryGenerator = () => repos.map((r) => ({ repo: r.name }));

export const load: PageLoad = ({ params }) => {
	const repo = getRepo(params.repo);
	if (!repo) error(404, `No release data for ${params.repo}`);
	return { repo };
};
