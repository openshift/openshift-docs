guard 'shell' do
  watch(/^.*\.adoc$/) { |m|
    if not m[0].start_with?('_preview') and not m[0].start_with?('_package')
      full_path      = m[0].split('/')
      src_group_path = full_path.length == 1 ? '' : full_path[0]
      filename       = full_path[-1][0..-6]
      system("bundle exec rake refresh_page['#{src_group_path}:#{filename}']")
    end
  }
end

guard 'livereload' do
  watch(%r{^_preview/.+\.(css|js|html)$})
  watch(%r{^_preview/.+\/.+\/.+\.(css|js|html)$})
end
