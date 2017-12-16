<<<<<<< HEAD
module.exports = {
	release: {
		options: {
			insertType: "prepend",
			template: "## Release v<%= package.version %>:\n\n{{> features}}{{> fixes}}\n\n",
			partials: {
				features: "#### Features:\n\n{{#if features}}{{#each features}}{{> feature}}{{/each}}{{else}}{{> empty}}{{/if}}\n",
				fixes: "#### Bugfixes:\n\n{{#if fixes}}{{#each fixes}}{{> fix}}{{/each}}{{else}}{{> empty}}{{/if}}",
				empty: " - (none)\n"
			},
			dest: "CHANGELOG.md"
		}
	}
=======
module.exports = {
	release: {
		options: {
			insertType: "prepend",
			template: "## Release v<%= package.version %>:\n\n{{> features}}{{> fixes}}\n\n",
			partials: {
				features: "#### Features:\n\n{{#if features}}{{#each features}}{{> feature}}{{/each}}{{else}}{{> empty}}{{/if}}\n",
				fixes: "#### Bugfixes:\n\n{{#if fixes}}{{#each fixes}}{{> fix}}{{/each}}{{else}}{{> empty}}{{/if}}",
				empty: " - (none)\n"
			},
			dest: "CHANGELOG.md"
		}
	}
>>>>>>> 5533bdf65d878a145647c5a627c74d872d536ee2
};