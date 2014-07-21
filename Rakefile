require 'asciidoctor'
require 'pandoc-ruby'
require 'pathname'
require 'rake'
require 'yaml'

BUILD_FILENAME  = '_build_cfg.yml'
BUILDER_DIRNAME = '_build_system'
PREVIEW_DIRNAME = '_preview'
PACKAGE_DIRNAME = '_package'
BLANK_STRING_RE = Regexp.new('^\s*$')

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

def build_config_file
  @build_config_file ||= File.join(source_dir,BUILD_FILENAME)
end

def build_config
  @build_config ||= validate_config(YAML.load_stream(open(build_config_file)))
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
    if not topic_group['Topics'].is_a?(Array)
      raise "The #{topic_group['Name']} topic group in #{build_config_file} is malformed; the build system is expecting an array of 'Topic' definitions."
    end
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
    end
  end
  config_data
end

def nav_tree
  @nav_tree ||= begin
    navigation = []
    build_config.each do |topic_group|
      topic_list = []
      topic_group['Topics'].each do |topic|
        topic_list << ["#{topic_group['Dir']}/#{topic['File']}.html",topic['Name']]
      end
      navigation << { :title => topic_group['Name'], :topics => topic_list }
    end
    navigation
  end
end

task :build do
  # Copy stylesheets into preview area
  system("cp -r _stylesheets #{preview_dir}/stylesheets")
  # Build the topic files
  build_config.each do |topic_group|
    src_group_path = File.join(source_dir,topic_group['Dir'])
    tgt_group_path = File.join(preview_dir,topic_group['Dir'])
    if not File.exists?(tgt_group_path)
      Dir.mkdir(tgt_group_path)
    end
    #if File.exists?(File.join(src_group_path,'images'))
    #  system("cp -r #{src_group_path}/images #{tgt_group_path}")
    #end
    topic_group['Topics'].each do |topic|
      src_file_path = File.join(src_group_path,"#{topic['File']}.adoc")
      tgt_file_path = File.join(tgt_group_path,"#{topic['File']}.adoc")
      system('cp', src_file_path, tgt_file_path)
      Asciidoctor.render_file tgt_file_path, :in_place => true, :safe => :unsafe, :template_dir => template_dir, :attributes => ['source-highlighter=coderay','coderay-css=style',"stylesdir=#{preview_dir}/stylesheets","imagesdir=#{src_group_path}/images",'stylesheet=origin.css','linkcss!','icons=font','idprefix=','idseparator=-','sectanchors']
      system('rm', tgt_file_path)
    end
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
  sh "rm -rf ../_preview ../_package" do |ok,res|
    if ! ok
      puts "Nothing to clean."
    end
  end
end
