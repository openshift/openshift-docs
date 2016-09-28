require 'ascii_binder/tasks/tasks'

task :import_api do
  base = ENV['ORIGIN_REPO'] || "../origin"
  sh "pushd #{base} && hack/update-swagger-docs.sh" do |ok,res|
    fail "Unable to generate docs" if !ok
  end
  sh "cp #{base}/_output/local/docs/swagger/api/v1/overview.adoc rest_api/kubernetes_v1.adoc" do |ok,res|
    fail "Unable to copy latest kubernetes v1 docs" if !ok
  end
  sh "cat #{base}/_output/local/docs/swagger/api/v1/{paths,definitions}.adoc >> rest_api/kubernetes_v1.adoc" do |ok,res|
    fail "Unable to concat latest kubernetes v1 docs" if !ok
  end
  sh "cp #{base}/_output/local/docs/swagger/oapi/v1/overview.adoc rest_api/openshift_v1.adoc" do |ok,res|
    fail "Unable to copy latest openshift v1 docs" if !ok
  end
  sh "cat #{base}/_output/local/docs/swagger/oapi/v1/{paths,definitions}.adoc >> rest_api/openshift_v1.adoc" do |ok,res|
    fail "Unable to concat latest openshift v1 docs" if !ok
  end
  puts "\nNOTE: You must edit rest_api/kubernetes_v1.adoc and rest_api/openshift_v1.adoc to add TOC metadata"
end
