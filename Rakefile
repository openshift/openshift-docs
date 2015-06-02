require "#{File.join(Dir.pwd,'_builder_lib/docsitebuilder/helpers')}"
require 'rake'

include DocSiteBuilder::Helpers

task :build, :build_distro do |task,args|
  # Figure out which distros we are building.
  # A blank value here == all distros
  build_distro = args[:build_distro] || ''
  generate_docs(build_distro)
end

task :package, :package_site do |task,args|
  package_site = args[:package_site] || ''
  Rake::Task["clean"].invoke
  Rake::Task["build"].invoke
  package_docs(package_site)
end

task :refresh_page, :single_page do |task,args|
  generate_docs('',args[:single_page])
end

task :clean do
  sh "rm -rf _preview/* _package/*" do |ok,res|
    if ! ok
      puts "Nothing to clean."
    end
  end
end

task :import_api do
  sh "pushd ../origin && hack/gen-swagger-docs.sh" do |ok,res|
    fail "Unable to generate docs" if !ok
  end
  sh "cp ../origin/_output/local/docs/swagger/api/v1/overview.adoc rest_api/kubernetes_v1.adoc" do |ok,res|
    fail "Unable to copy latest kubernetes v1 docs" if !ok
  end
  sh "cat ../origin/_output/local/docs/swagger/api/v1/{paths,definitions}.adoc >> rest_api/kubernetes_v1.adoc" do |ok,res|
    fail "Unable to concat latest kubernetes v1 docs" if !ok
  end
  sh "cp ../origin/_output/local/docs/swagger/oapi/v1/overview.adoc rest_api/openshift_v1.adoc" do |ok,res|
    fail "Unable to copy latest openshift v1 docs" if !ok
  end
  sh "cat ../origin/_output/local/docs/swagger/oapi/v1/{paths,definitions}.adoc >> rest_api/openshift_v1.adoc" do |ok,res|
    fail "Unable to concat latest openshift v1 docs" if !ok
  end
  puts "\nNOTE: You must edit rest_api/kubernetes_v1.adoc and rest_api/openshift_v1.adoc to add TOC metadata"
end