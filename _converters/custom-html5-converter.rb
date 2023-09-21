require 'asciidoctor'

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
    @branch_name = ENV.fetch("GIT_CURR_BRANCH", `git rev-parse --abbrev-ref HEAD`.strip)
    @github_repo = ENV.fetch("GIT_CURR_REPO", "openshift/openshift-docs")
    super
  end

  # Focusing on "section" conversions prevent including modules
  # for content such as "snippets", etc. and focuses primarily
  # on modules
  def convert_section node
    parent_output = super
    begin
      unless node.source_location.nil?
        if @seen_files.empty? || !@seen_files.include?(node.source_location.path)
          @seen_files << node.source_location.path
          %(<div class="edit-section-button">
  <a href="https://github.com/#{@github_repo}/edit/#{@branch_name}/#{node.source_location.path}" target="_blank"><span class="material-icons-outlined" title="Edit section module">edit</span></a>
</div>
#{ parent_output })
        end
      end
    rescue NoMethodError
      parent_output
    end
  end
end