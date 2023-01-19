# Contributor Guide

## Requirements

To contribute to this project, you will need the [Hugo](https://gohugo.io/)
static site generation framework.  Follow the instructions on the
[Install Hugo](https://gohugo.io/getting-started/installing/) page for how
to install Hugo on your own system.  The
[Getting Started](https://gohugo.io/categories/getting-started) section
of the documentation will help you understand the Hugo system and how to
configure and use it.

## Building the site locally

This is a static site built with Hugo. Hugo has a built-in webserver so you can
test your build locally.

To build the site on your machine:

````
git clone https://github.com/NCAR/vast.git
cd vast
hugo serve
````

You will see something like this:

````
Start building sites …
hugo v0.97.3+extended darwin/amd64 BuildDate=unknown

                   | EN
-------------------+------
  Pages            |  39
  Paginator pages  |   1
  Non-page files   |   0
  Static files     | 203
  Processed images |   0
  Aliases          |   7
  Sitemaps         |   1
  Cleaned          |   0

Built in 360 ms
Watching for changes in /Users/kpaul/Software/Development/vast-web/{archetypes,content,data,layouts,static,themes}
Watching for config changes in /Users/kpaul/Software/Development/vast-web/config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
````

Using your favorite browser, navigate to ` http://localhost:XXXX/` where `XXXX` is the port number given in the hugo message.  Hugo uses live reload, so as you edit your files, the site will be continuously rebuilt.

## Adding content

The Hugo site directory structure looks like this:

````
.
├── config.yml
├── content/
├── data/
└── static/
````

The following are used when adding content to the website:

- The `config.yml` file contains site wide settings, such as the base-url and the navigation
  items on both the header and footer.  This almost never needs to change unless the navigation
  menus needs to be modified.

- The `content` directory contains the website pages. Each subdirectory is a section of the
  website, pertaining to a specific page with the same name as the subdirectory.  The `_index.md`
  file in each subdirectory contains a header section (at the top between two lines of `---`) containing metadata such as the page `title`, `date` of creation, and page header background `image`.  Some other pages have specific metadata fields that are required for the page to display correctly.

  Below the header in the `_index.md` file is the page `Content`.  Some pages do not display
  anything from the `Content` section of the file, as their contents are automatically generated.

- The `data` directory contains data (in YAML file format) that is used to automatically
  generate content on different sections of the website, such as the information about
  individual team members or team metrics or publications.

- The `static` directory contains files used in the website as-is, such as images.

### Modifying Site Data

The following details what site content you can add or change by changing data files in the
`data` directory.

#### Adding a new team member

Edit `data/team.yml` to add a new team member

````
  - name        : JOHN CLYNE
    designation : Senior Program Manager
    ncaruname   : clyne
    githubuname : clyne
````

Each team member card on the `about` page will be automatically generated based on the contents
of this data file.

#### Adding publications

Edit `data/publications.yml` to add a new publication citation:

````
  - title: Some journal article title.
    authors:
      - Bellew, A.
      - Darrow, C
      - Groves, E. F.
    journal: The Journal of Stuff
    year: 2003
    extra: "1(2):3-4"
    url: https://example.com
````

The `extra` field is optional and can contain journal volume information and page numbers.
If the `url` field is specified, then the citation will hyperlink to the given URL.

#### Adding presentations

Edit `data/presentations.yml` to add a new presentation or publication citation:

````
  - title: Some presentation title.
    authors:
      - Last, F.
    conference: The Most Prestigious Conference
    year: 2023
    extra: City, ST
    url: https://example.com
````

The `extra` field is optional and can contain conference city, virtual nature, or any other information.

Please specify the `url` field to be a link to a PDF file of the talk slides or poster uploaded to the [VAST Presentations Google Drive fodler](https://drive.google.com/drive/folders/146ZZgV5Pb0-scadJtrPEXfP_jhDYwKVL). Please use a naming convention akin to `Last_Topic_ConferenceYYYY` and be sure that the file's sharing settings allow anyone to view the file.

#### Adding services

Services provided by VAST can be listed in the `data/services.yml` data file, which is used
to automatically create the **SERVICES** section on the website home page.

Separately, you can add a larger writeup about services provided by VAST in the
`content/_index.md` file's `Content` section.

#### Adding metrics

VAST metrics are displayed in the **METRICS** section of the website home page (near the
bottom).  These metrics can be updates by modifying (or adding to) the `data/metrics.yml`
data file.

### Adding or Modifying Site Pages

The following describes how to add (or modify) pages to the site in the main sections
available from the site navigation menu:

- About
- Education
- News (blog)
- Projects (R&D)
- Software

#### Modifying the VAST About page

Just modify the `Content` section (i.e., everything under the header) of the
`content/about/_index.md` file.  The VAST mission statement (formatted differently
on the about page) can be modified by changing the `mission` field in the header.

At the bottom of the About page is the VAST team section, which can be modified by changing the `data/team.yml` file (see above).

#### Modifying the VAST Education page

Just modify the `Content` section (i.e., everything under the header) of the
`content/education/_index.md` file.

#### Modifying the VAST Services page

Just modify the `Content` section (i.e., everything under the header) of the
`content/services/_index.md` file.

#### Adding a new blog

To create a new blog entry, just use the `hugo` command line to create a new
markdown file for the blog entry:

````
hugo new news/my-new-blog-post.md
````

This creates the `content/news/my-new-blog-post.md` file, and you can edit the
header and contents of the file to display the blog.  This blog will be displayed
on the main blog page with the thumbnail image and its title.

#### Adding a new project to the VAST R&D page

To create a new project description, just use the `hugo` command line to create a new
markdown file for the project description:

````
hugo new projects/my-project.md
````

This creates the `content/projects/my-project.md` file, and you can edit the
header and contents of the file to change the detailed description of the project.
This project will be displayed in the **RECENT PROJECTS** section of the main
website home page and on the **VAST R&D** page.

#### Adding a new software product to the VAST Software page

To create a new software product description, just use the `hugo` command line to create a new
markdown file for the software product:

````
hugo new software/my-product.md
````

This creates the `content/software/my-product.md` file, and you can edit the
header and contents of the file to change the detailed description of the software product.
This project will be displayed in the scrolling carousel of software products at the
top of the website home page and on the **VAST Software** page.

### Using Jupyter Notebooks rather than markdown

I haven't explored this, but Jupyter Notebooks can be used for content on a Hugo
website using the [Hugo Jupyter](https://knowsuchagency.github.io/hugo_jupyter/)
utility.

### Using NCAR icons

You can use NCAR icons.  To see a demo of all the NCAR icons available,

````
open themes/ncar/static/icomoon/demo.html
````

To use a particular icon:

````
<span class="icon-data-assimilation"></span>
````

## ADVANCED CONTENT

All of the layout and structure of the site is built into the `themes/ncar` Hugo
Theme, which is contained in this repository.  If the structure of the website,
such as the addition of new sections on the landing page or special new pages pointed to
by the navigation menu, you might need to create a Hugo Layout for it to work.  And
this will also entail creating new CSS.

In addition to the directories described above, the Hugo directory structure contains
a directory called `themes`, inside of which is the `ncar` theme that is used for this
site.  Modification of the theme is the only way of properly add completely new sections
to the website.

Within the `themes/ncar` directory, there are the following directories:

````
.
├── archetypes/
├── assets/
├── layouts/
└── static/
````

- The `archetypes` directory contains markdown files that serve as templates (stubs) for
  new pages, such as when you use `hugo new ...`.  If you create a new page with the
  command `hugo new foo/bar.md`, then the new file that is created will be a copy of the
  `archetypes/foo.md` file.

- The `assets` directory contains any JS, CSS or SASS (SCSS) that needs to be processed before
  adding it to the website's `static` directory.  SASS files need to be compiled, and some
  JS and CSS may need to be *minified* before adding them to the site's static files.  The
  `assets/scss/` directory contains custom SCSS for the site, so if new sections are created
  for the website (i.e., by adding a new *layout*, described below), you can add the new
  SCSS for styling those new sections here.

- The `layouts` directory contains `.html` layouts (i.e., Hugo templates).  These templates
  describe how to place information constructed from the conversion of markdown to HTML or the
  reading of data from `data` files into the proper structure for display on the website.  Each section on the site corresponds to a matching named directory in the `layouts` folder of the
  theme.  Within these subdirectories, a `list.html` file is used to display pages that
  contain a list of other content (e.g., the list of all blog posts).  The `single.html` file
  describes how to render single pages within the section (e.g., a single blog post).

  The `layouts/partials` directory is special.  It contains templated HTML that can be reused in different places of the site, simply by *importing* the template into another template (e.g.,
  the Hugo templating `{{ partial "mypartial.html" }}` paradigm).

  The `layouts/_default` directory contains the defaults for all pages.

- The `static` directory contains all static files (merged with the higher-level `static`
  directory) that are specific to the theme (and not the website).

**TODO**: If the `themes/ncar` theme works and does not require significant modification, then
it should probably be rolled into its own repository and included in this repository as a git
submodule, which is the canonical way of adding themes to a Hugo site.

## Known Issues

- The Hugo server (`hugo serve`) does not seem to properly deal with some of the JS that
  ships with the theme.  However, it works on the GitHub pages site, so it's not a huge
  concern.
