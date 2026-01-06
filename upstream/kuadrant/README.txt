Managing content from upstream Kuadrant projects
------------------------------------------------

This directory contains the content from upstream Kuadrant GitHub projects (https://github.com/kuadrant). To use and maintain the content from this upstream repository, you need to know about the following routine tasks:

Fetch the latest content from the upstream repositories
-------------------------------------------------------
1. cd docs/upstream/kuadrant
2. ./fetch-upstream.sh

Include modules or assemblies in your guide
-------------------------------------------
Prerequisites:
* Your guide directory must have a symbolic link to the docs/upstream/kuadrant directory.
* The docs/upstream/kuadrant/attributes.adoc file has the required variables to define base directories for all categories of upstream content.

1. The attributes for the base directories have the general form of: 
 - kuadrant-UPSTREAM-CATEGORY-module
 - kuadrant-UPSTREAM-CATEGORY-assembly
 - kuadrant-CATEGORY-image

2. For example, to include an assembly from the 'getting-started' category from the kuadrant upstream:
include::{kuadrant-getting-started-assembly}/as_installing-kuadrant.adoc[leveloffset=+1]

Incorporate a new upstream category in your guide
-------------------------------------------------
From time to time, the upstream project might create a new category (effectively, a new directory or subdirectory containing module or assembly content). 
To incorporate this new content:

1. Fetch the latest upstream content (including content from the new category):
./fetch-upstream.sh

2. Edit the attributes.adoc file in docs/upstream/kuadrant and define three new attributes for the category, following this template:
:kuadrant-UPSTREAM-CATEGORY-module: upstream/kuadrant/kuadrant-{branch}/path/to/new/category
:kuadrant-UPSTREAM-CATEGORY-assembly: upstream/kuadrant/kuadrant-{branch}/path/to/new/category
:kuadrant-UPSTREAM-CATEGORY-image: upstream/kuadrant/kuadrant-{branch}/path/to/new/category

3. If the new category includes images, create a symbolic link under your BOOK_DIR/images directory to gain access to the relevant images directory. 
For example, if you are trying to access the CATEGORY category from the kuadrant upstream:

cd BOOK_DIR/images
ln -s ../../upstream/kuadrant/kuadrant-master/docs/images/CATEGORY CATEGORY

4. Edit your BOOK_DIR/master.adoc file to include assemblies from the kuadrant upstream, using the attributes from the kuadrant attributes.adoc file. 
For example, if you want to include the 'as_installing-the-kuadrant' assembly from the 'getting-started' category of the kuadrant upstream:

include::{kuadrant-getting-started-assembly}/as_installing-the-kuadrant.adoc[leveloffset=+1] 

Create a new guide that references the kuadrant upstream
--------------------------------------------------------
To create a new guide that references the kuadrant upstream content:

1. Create the basic guide directory using Nebel:
nebel guide --create BOOK_DIR

2. Create a subdirectory for upstream content:
mkdir BOOK_DIR/upstream

3. Create a symbolic link to the kuadrant upstream directory:
cd BOOK_DIR/upstream
ln -s ../../upstream/kuadrant kuadrant

4. Create symbolic links to the images subdirectories. In the case of the kuadrant upstream, there is a different images subdirectory for each category, 
so you will potentially need to create multiple symbolic links. For example, if you guide needs to access images from the 'getting-started' category, 
you would create the symbolic link as follows:

cd BOOK_DIR/images
ln -s ../../upstream/kuadrant/kuadrant-master/doc/images/getting-started getting-started

5. Edit the BOOK_DIR/master.adoc file to include the attributes.adoc file from kuadrant. For example, add the following line at the top of the 
master.adoc file:

include::upstream/kuadrant/attributes.adoc[]

6. Edit the BOOK_DIR/master.adoc file to include assemblies from the kuadrant upstream, using the attributes from the kuadrant attributes.adoc file. 
For example:

include::{kuadrant-getting-started-assembly}/as_installing-the-kuadrant.adoc[leveloffset=+1]

Defining a Pantheon title for a guide that uses kuadrant content upstream
-------------------------------------------------------------------------
When defining a new Pantheon title for a guide using kuadrant content, you need to include the following "extra content directory" in the title 
definition:

docs/upstream/kuadrant
