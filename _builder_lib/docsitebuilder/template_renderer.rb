require 'tilt'

module DocSiteBuilder
  class TemplateRenderer
    def self.template_cache
      @template_cache ||= {}
    end

    def self.initialize_cache(directory)
      Dir.glob(File.join(directory, "**/*")).each do |file|
        template_cache[file] = Tilt.new(file, :trim => "-")
      end
    end

    def render(template, args = {})
      renderer_for(template).render(self, args).chomp
    end

    private

    def renderer_for(template)
      self.class.template_cache.fetch(File.expand_path(template))
    end
  end
end
