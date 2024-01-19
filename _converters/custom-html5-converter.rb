require 'asciidoctor'
require 'ascii_binder/distro_map'
require 'ascii_binder/helpers'

include AsciiBinder::Helpers

Asciidoctor::Document.prepend (Module.new do
  attr_writer :sourcemap
end) unless Asciidoctor::Document.method_defined? :sourcemap=

# A preprocessor that enables the sourcemap feature if not already enabled via the API.
Asciidoctor::Extensions.register do
  preprocessor do
    process do |doc, reader|
      doc.sourcemap = true
      nil
    end
  end
end

class CustomHtml5Converter < (Asciidoctor::Converter.for 'html5')
  register_for 'html5'

  def initialize backend, opts = {}
    # A new converter is initialized for every new assembly file
    # Create a new set to prevent showing multiple edit buttons for the
    # same module file
    @seen_files = Set.new
    @branch_name = ENV.fetch("GIT_BRANCH", "main")
    @github_repo = ENV.fetch("GIT_REPO", "openshift/openshift-docs")
    distro_edit_enabled = ENV.fetch("DISTRO_EDIT_ENABLED", "").split(",")
    distro_map = AsciiBinder::DistroMap.new(File.join(docs_root_dir, DISTRO_MAP_FILENAME))
    # current_distro will be `nil` if not intersect is found
    current_distro = (distro_map.distro_keys & opts[:document].attributes.keys).first
    @show_edit_button = distro_edit_enabled.include? current_distro
    super
  end

  # "embedded" seems to capture a fully complete document,
  # so placing an edit button at the top encompasses a whole-page
  # edit
  def convert_embedded node
    parent_output = super
    if @show_edit_button && node.source_location.nil?
      %(<div class="edit-page-button edit-button">
    <a href="https://github.com/#{ @github_repo }/edit/#{ @branch_name }/#{ node.attributes["repo_path"] }" target="_blank">
      <span class="material-icons-outlined" title="Suggest a page edit">edit</span>
    </a>
  </div>
  #{ parent_output })
    else
      parent_output
    end
  end

  # Focusing on "section" conversions prevent including modules
  # for content such as "snippets", etc. and focuses primarily
  # on modules
  def convert_section node
    parent_output = super
    if @show_edit_button && node.source_location
      file_path = node.source_location.path.include?("modules") ? node.source_location.path : node.source_location.file.sub(node.source_location.dir + "/", "")

      if @seen_files.empty? || !@seen_files.include?(file_path)
        @seen_files << file_path
        return %(<div class="edit-section-button edit-button">
    <a href="https://github.com/#{ @github_repo }/edit/#{ @branch_name }/#{ file_path }" target="_blank">
      <span class="material-icons-outlined" title="Suggest a section edit">edit</span>
    </a>
  </div>
  #{ parent_output })
      end
    end
    parent_output
  end
end
