# Security Research Artifacts (secartifacts)

The [secartifacts website](https://secartifacts.github.io/) hosts the artifact evaluation of multiple conferences.
While initially for SOSP'19, the website was generalized to also host the AEs for other systems conferences.
As part of the generalization we changed from static HTML pages to a Jekyll-rendered site.
This process is integrated into GitHub Pages.
This repository includes the sources for Jekyll to render the HTML pages.


## Contributing

You can contribute to this website and repository via pull requests. 
Please fork the [GitHub repository](https://github.com/secartifacts/secartifacts.github.io),
modify the respective files, and submit a pull request from your personal branch.
In the pull request, please describe your changes and any reasons for the changes.
Once reviewed it will be merged and available on the secartifacts website.


We ask you to build the repository and preview your changes before submitting the pull request.
You have three options to preview changes: 
* configure your forked repository on GitHub to use your branch for GitHub Pages
  and view it at `your_username.github.io/secartifacts.github.io`
* install Jekyll and Bundler locally then run `bundle exec jekyll serve` at the root of the repository
* build the repository via [jekyll's docker container](https://github.com/envygeeks/jekyll-docker), for example using
  the following command to start a jekyll server on [http://localhost:4000/](http://localhost:4000/):
  ``` sh
  docker run --rm --volume="$PWD:/srv/jekyll" -p 4000:4000 jekyll/jekyll jekyll serve
  ```

## Adding an additional conference

We welcome other security conferences and workshops to join the efforts to make security artifacts easily accessible.

To add a conference, copy the `.md` in `_conferences` from one of the existing conferences
(e.g. `usesec.md`) in the root folder to your conference name (e.g. `sp.md`).
This will lead to creating `sp.html` when rendered.
Adapt this page to your conference name by changing the title and text (e.g. change `USENIX Security` to `IEEE S&P`).


## Adding another year to an existing conference

Start from an existing conference year such as `eurosys2022`, by
copy-pasting its existing folder in `_conferences` to your new folder.
The folder name must be the exact conference name followed by the year such as `atc2022` for `atc` in `2022`.

Pages are in Kramdown ([cheat sheet](https://kramdown.gettalong.org/quickref.html)).

To change the order of items in the left sidebar, change the `order` property in the front matter.
