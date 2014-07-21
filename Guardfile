require 'asciidoctor'
require 'erb'
require 'haml'
require 'tilt'

guard 'shell' do
  watch(/^.*\.adoc$/) { |m|
    if not m[0].start_with?('_preview')
      src_group_path = m[0].split('/')[0]
      filename       = m[0].split('/')[-1][0..-6]
      tgt_file_path  = "_preview/#{src_group_path}"
      Asciidoctor.render_file m[0], :in_place => true, :safe => :unsafe, :template_dir => '_template', :attributes => ['source-highlighter=coderay','coderay-css=style',"stylesdir=_preview/stylesheets","imagesdir=#{src_group_path}/images",'stylesheet=origin.css','linkcss!','icons=font','idprefix=','idseparator=-','sectanchors']
      system('mv', "#{src_group_path}/#{filename}.html", "#{tgt_file_path}/")
    end
  }
end

guard 'livereload' do
  watch(%r{^_preview\.(css|js|html)$})
end
