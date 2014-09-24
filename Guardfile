guard 'shell' do
  watch(/^.*\.adoc$/) { |m|
    if not m[0].start_with?('_preview')
      src_group_path = m[0].split('/')[0]
      filename       = m[0].split('/')[-1][0..-6]
      system("bundle exec rake refresh_page['#{src_group_path}:#{filename}']")
    end
  }
end

guard 'livereload' do
  watch(%r{^_preview/.+\.(css|js|html)$})
  watch(%r{^_preview/.+\/.+\/.+\.(css|js|html)$})
end
