require 'asciidoctor'
require 'git'
require 'logger'
require 'pandoc-ruby'
require 'pathname'
require 'rake'
require 'yaml'

BUILD_FILENAME  = '_build_cfg.yml'
BUILDER_DIRNAME = '_build_system'
PREVIEW_DIRNAME = '_preview'
PACKAGE_DIRNAME = '_package'
BLANK_STRING_RE = Regexp.new('^\s*$')
PRODUCT_AUTHOR  = "OpenShift Documentation Project <dev@lists.openshift.redhat.com>"

def source_dir
  @source_dir ||= File.expand_path(Dir.pwd)
end

def template_dir
  @template_dir ||= File.join(source_dir,'_templates')
end

def preview_dir
  @preview_dir ||= begin
    preview_dir = File.join(source_dir,PREVIEW_DIRNAME)
    if not File.exists?(preview_dir)
      Dir.mkdir(preview_dir)
    end
    preview_dir
  end
end

def package_dir
  @package_dir ||= begin
    package_dir = File.join(source_dir,PACKAGE_DIRNAME)
    if not File.exists?(package_dir)
      Dir.mkdir(package_dir)
    end
    package_dir
  end
end

def git
  @git ||= Git.open(source_dir)
end

def git_checkout branch_name
  target_branch = git.branches.local.select{ |b| b.name == branch_name }[0]
  if not target_branch.current
    target_branch.checkout
  end
end

# Returns the local git branches; current branch is always first
def local_branches
  @local_branches ||= begin
    branches = []
    branches << git.branches.local.select{ |b| b.current }[0].name
    branches << git.branches.local.select{ |b| not b.current }.map{ |b| b.name }
    branches.flatten
  end
end

def build_config_file
  @build_config_file ||= File.join(source_dir,BUILD_FILENAME)
end

def build_config
  @build_config ||= validate_config(YAML.load_stream(open(build_config_file)))
end

def distro_map
  @distro_map ||= begin
    { 'openshift-origin' => {
        :name     => 'OpenShift Origin',
        :branches => {
          'master'   => {
            :name => 'Nightly Build',
            :dir  => 'latest',
          },
          'origin-4' => {
            :name => 'Version 4',
            :dir  => 'stable',
          },
        },
      },
      'openshift-online' => {
        :name     => 'OpenShift Online',
        :branches => {
          'online' => { 
            :name => 'Latest Release',
            :dir  => 'online',
          },
        },
      },
      'openshift-enterprise' => {
        :name     => 'OpenShift Enterprise',
        :branches => {
          'enterprise-2.2' => {
            :name => 'Version 2.2',
            :dir  => 'enterprise/v2.2',
          },
        },
      }
    }
  end
end

def distro_branches
  @distro_branches ||= distro_map.map{ |distro,dconfig| dconfig[:branches].keys }.flatten
end

def page(args)
  page_css = ''
  args[:css].each do |sheet|
    sheet_href = args[:css_path] + sheet
    page_css << "<link href=\"#{sheet_href}\" rel=\"stylesheet\" />\n"
  end
  page_head = <<EOF
<!DOCTYPE html>
<html>
<head>
<title>#{args[:distro]} #{args[:version]} | #{args[:group_title]} | #{args[:topic_title]}</title>
#{page_css}
<script src="http://code.jquery.com/jquery-2.1.1.min.js"></script>
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
</head>
<body>
<div class="container">
  <h3>OpenShift Documentation <small>#{args[:distro]} #{args[:version]}</small></h3>
  <div class="row">
    <div class="col-md-3">
      <form method="get" onsubmit="window.location.href='https://www.google.com/search?as_q=' + this.elements.docsSearch.value + '&as_sitesearch=openshift.github.io';">
      <div class="input-group">
        <!-- <span class="input-group-addon"><span class="glyphicon glyphicon-search"></span></span> //-->
        <input id="docsSearch" name="docsSearch" type="text" class="form-control" />
        <span class="input-group-btn">
          <button class="btn btn-default" type="button" onclick="window.location.href='https://www.google.com/search?as_q=' + this.form.elements.docsSearch.value + '&as_sitesearch=openshift.github.io';">Search</button>
        </span>
      </div>
      <p>&nbsp;</p>
      </form>
EOF

  page_nav = ['      <div class="panel-group">']
  groupidx = 0
  args[:navigation].each do |topic_group|
    current_group = topic_group[:id] == args[:group_id]
    page_nav << '        <div class="panel panel-default">'
    page_nav << '          <div class="panel-heading">'
    page_nav << '            <h3 class="panel-title">'
    page_nav << "              <a data-toggle=\"collapse\" data-parent=\"#accordion\" href=\"#topicGroup#{groupidx}\">#{topic_group[:name]}</a>"
    page_nav << '            </h3>'
    page_nav << '          </div>'
    page_nav << "          <ul id=\"topicGroup#{groupidx}\" class=\"list-group panel-collapse collapse#{current_group ? ' in' : ''}\">"
    topic_group[:topics].each do |topic|
      current_topic = topic[:id] == args[:topic_id]
      page_nav << "            <li class=\"list-group-item\"><a class=\"list-group-item#{current_topic ? ' active' : ''}\" href=\"#{topic[:path]}\">#{topic[:name]}</a></li>"
    end
    page_nav << '          </ul>'
    page_nav << '        </div>'
    groupidx = groupidx + 1
  end
  page_nav << '      </div>'

  page_body = <<EOF
    </div>
    <div class="col-md-9">
      <div class="page-header">
        <h2>#{args[:group_title]}: #{args[:topic_title]}</h2>
      </div>
      #{args[:content]}
    </div>
  </div>
</div>
</body>
</html>
EOF

  page_txt = ''
  page_txt << page_head
  page_txt << "\n"
  page_txt << page_nav.join("\n")
  page_txt << "\n"
  page_txt << page_body
  page_txt
end

def parse_distros distros_string, for_validation=false
  values = distros_string.split(',').map{ |v| v.strip }
  return values if for_validation
  return distro_map.keys if values.include?('all')
  return values.uniq
end

def validate_distros distros_string
  return false if not distros_string.is_a?(String)
  values = parse_distros(distros_string, true)
  values.each do |v|
    return false if not v == 'all' or not distro_map.keys.include?(v)
  end
  return true
end

def validate_config config_data
  # Validate/normalize the config file straight away
  if not config_data.is_a?(Array)
    raise "The configutaration in #{build_config_file} is malformed; the build system is expecting an array of topic groups."
  end
  config_data.each do |topic_group|
    # Check for presence of topic group keys
    ['Name','Dir','Topics'].each do |group_key|
      if not topic_group.has_key?(group_key)
        raise "One of the topic groups in #{build_config_file} is missing the '#{group_key}' key."
      end
    end
    # Check for right format of topic group values
    ['Name','Dir'].each do |group_key|
      if not topic_group[group_key].is_a?(String)
        raise "One of the topic groups in #{build_config_file} is not using a string for the #{group_key} setting; current value is #{topic_group[group_key].inspect}"
      end
      if topic_group[group_key].empty? or topic_group[group_key].match BLANK_STRING_RE
        raise "One of the topic groups in #{build_config_file} is using a blank value for the #{group_key} setting."
      end
    end
    if not File.exists?(File.join(source_dir,topic_group['Dir']))
      raise "In #{build_config_file}, the directory #{topic_group['Dir']} for topic group #{topic_group['Name']} does not exist under #{source_dir}"
    end
    # Validate the Distros setting
    if topic_group.has_key?('Distros')
      if not validate_distros(topic_group['Distros'])
        key_list = distro_map.keys.map{ |k| "'#{k.to_s}'" }.sort.join(', ')
        raise "In #{build_config_file}, the Distros value #{topic_group['Distros'].inspect} for topic group #{topic_group['Name']} is not valid. Legal values are 'all', #{key_list}, or a comma-separated list of legal values."
      end
      topic_group['Distros'] = parse_distros(topic_group['Distros'])
    else
      topic_group['Distros'] = parse_distros('all')
    end
    if not topic_group['Topics'].is_a?(Array)
      raise "The #{topic_group['Name']} topic group in #{build_config_file} is malformed; the build system is expecting an array of 'Topic' definitions."
    end
    # Generate an ID for this topic group
    topic_group['ID'] = camelize topic_group['Name']
    # Now buzz through the topics
    topic_group['Topics'].each do |topic|
      ['Name','File'].each do |topic_key|
        if not topic[topic_key].is_a?(String)
          raise "In #{build_config_file}, topic group #{topic_group['Name']}, one of the topics is not using a string for the '#{topic_key}' setting; current value is #{topic[topic_key].inspect}"
        end
        if topic[topic_key].empty? or topic[topic_key].match BLANK_STRING_RE
          raise "In #{build_config_file}, topic group #{topic_group['Name']}, one of the topics is using a blank value for the '#{topic_key}' setting"
        end
      end
      # Normalize the filenames
      if topic['File'].end_with?('.adoc')
        topic['File'] = topic['File'][0..-6]
      end
      if not File.exists?(File.join(source_dir,topic_group['Dir'],"#{topic['File']}.adoc"))
        raise "In #{build_config_file}, could not find file #{topic['File']} under directory #{topic_group['Dir']} for topic #{topic['Name']} in topic group #{topic_group['Name']}."
      end
      if topic.has_key?('Distros')
        if not validate_distros(topic['Distros'])
          key_list = distro_map.keys.map{ |k| "'#{k.to_s}'" }.sort.join(', ')
          raise "In #{build_config_file}, the Distros value #{topic_group['Distros'].inspect} for topic item #{topic['Name']} in topic group #{topic_group['Name']} is not valid. Legal values are 'all', #{key_list}, or a comma-separated list of legal values."
        end
        topic['Distros'] = parse_distros(topic['Distros'])
      else
        topic['Distros'] = parse_distros('all')
      end
      # Generate an ID for this topic
      topic['ID'] = "#{topic_group['ID']}::#{camelize(topic['Name'])}"
    end
  end
  config_data
end

def camelize text
  text.split(' ').map{ |t| t.capitalize }.join
end

def nav_tree distro
  @nav_tree ||= begin
    navigation = []
    build_config.each do |topic_group|
      next if not topic_group['Distros'].include?(distro)
      next if topic_group['Topics'].select{ |t| t['Distros'].include?(distro) }.length == 0
      topic_list = []
      topic_group['Topics'].each do |topic|
        next if not topic['Distros'].include?(distro)
        topic_list << {
          :path => "../#{topic_group['Dir']}/#{topic['File']}.html",
          :name => topic['Name'],
          :id   => topic['ID'],
        }
      end
      navigation << { :name => topic_group['Name'], :id => topic_group['ID'], :topics => topic_list }
    end
    navigation
  end
end

task :build do
  # First, notify the user of missing local branches
  missing_branches = []
  distro_branches.sort.each do |dbranch|
    next if local_branches.include?(dbranch)
    missing_branches << dbranch
  end
  if missing_branches.length > 0
    puts "\nNOTE: The following branches do not exist in your local git repo:"
    missing_branches.each do |mbranch|
      puts "- #{mbranch}"
    end
    puts "The build will proceed but these branches will not be generated."
  end
  distro_map.each do |distro,distro_config|
    puts "\n\nBuilding #{distro_config[:name]}"
    distro_config[:branches].each do |branch,branch_config|
      if missing_branches.include?(branch)
        puts "- skipping #{branch}"
        next
      end
      puts "- building #{branch}"

      # Put us on the correct branch
      git_checkout(branch)

      # Create the target dir
      branch_path = "#{preview_dir}/#{branch_config[:dir]}"
      system("mkdir -p #{branch_path}/stylesheets")

      # Copy stylesheets into preview area
      system("cp -r _stylesheets/*css #{branch_path}/stylesheets")

      # Build the landing page
      navigation = nav_tree(distro)

      # Build the topic files
      build_config.each do |topic_group|
        next if not topic_group['Distros'].include?(distro)
        next if topic_group['Topics'].select{ |t| t['Distros'].include?(distro) }.length == 0
        src_group_path = File.join(source_dir,topic_group['Dir'])
        tgt_group_path = File.join(branch_path,topic_group['Dir'])
        if not File.exists?(tgt_group_path)
          Dir.mkdir(tgt_group_path)
        end
        topic_group['Topics'].each do |topic|
          next if not topic['Distros'].include?(distro)
          puts "  - #{topic['ID']}"
          src_file_path = File.join(src_group_path,"#{topic['File']}.adoc")
          tgt_file_path = File.join(tgt_group_path,"#{topic['File']}.html")
          topic_adoc    = File.open(src_file_path,'r').read
          topic_html    = Asciidoctor.render topic_adoc, :header_footer => false, :safe => :unsafe, :attributes => ['source-highlighter=coderay','coderay-css=style',"imagesdir=#{src_group_path}/images",'linkcss!','icons=font','idprefix=','idseparator=-','sectanchors', distro, "product-title=#{distro_config[:name]}", "product-version=#{branch_config[:name]}", "product-author=#{PRODUCT_AUTHOR}"]
          full_file_text = page({
            :distro      => distro_config[:name],
            :version     => branch_config[:name],
            :group_title => topic_group['Name'],
            :topic_title => topic['Name'],
            :content     => topic_html,
            :navigation  => navigation,
            :group_id    => topic_group['ID'],
            :topic_id    => topic['ID'],
            :css_path    => "#{branch_path}/stylesheets/",
            :css         => [
              'bootstrap_default.min.css',
              'font-awesome.min.css',
              'foundation.css',
              'origin.css',
            ]
          })
          File.write(tgt_file_path,full_file_text)
        end
      end
    end

    # Return to the original branch
    git_checkout(local_branches[0])
  end
end

task :package do
  builds = [
    { :branch => 'master',
      :branch_dir  => ['/','openshift_origin/nightly'],
      :doc_version => 'OpenShift Origin Latest'
    },
  ]

  branches = `git branch`.split(/\n/).map{ |branch| branch.strip }

  # Remeber the working branch so that we can return here later.
  working_branch = 'master'
  branches.each do |branch|
    next if not branch.start_with?('*')
    working_branch = branch.sub!(/^\* /,'')
  end

  # Make sure the working branch doesn't have any uncommitted changes
  changed_files = `git status --porcelain`
  if not changed_files.empty?
    puts "Warning: Your current branch has uncommitted changes. Hit <CTRL+C> if you want to exit."
    print "Starting packager in "
    [3,2,1].each do |i|
      print "#{i}..."
      sleep 1
    end
    print "\n"
  end

  # Now make sure the build branches are available.
  missing_branches = false
  builds.each do |build|
    if not branches.include?(build[:branch])
      if not missing_branches
        puts "ERROR: One or more branches for packaging are not available in this local repo:"
        missing_branches = true
      end
      puts "- #{build[:branch]}"
    end
  end
  if missing_branches
    puts "Add these branches and rerun the packaging command."
    exit 1
  end

  # Start packaging. Clear out the old package dir before making the new package
  if Dir.entries('..').include?('_package')
    system 'rm', '-rf', '../_package'
  end
  Dir.mkdir('../_package')

  # Now make each package.
  builds.each do |build|
    # Check out this build branch
    system("git checkout #{build[:branch]}")

    if not $?.exitstatus == 0
      puts "ERROR: Could not check out branch #{build[:branch]}, please investigate."
      exit 1
    end

    # Make the build dir
    build_dir = "../_package/#{build[:site_dir]}"
    Dir.mkdir(build_dir)

    # Build the docs
    Rake::Task['build'].execute

    # Clean everything up
    Rake::Task['clean'].execute
  end

  # Return to the original branch
  system("git checkout #{working_branch}")

  puts "Packaging completed."
end

task :clean do
  sh "rm -rf _preview/* _package/*" do |ok,res|
    if ! ok
      puts "Nothing to clean."
    end
  end
end
