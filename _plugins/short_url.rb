# _plugins/short_url.rb
require 'digest'

# 1. 注册最高优先级的 :post_init 钩子（在初始化文章数据时就写入 permalink）
Jekyll::Hooks.register :posts, :post_init do |post|
  unique_key = post.relative_path
  short_hash = Digest::MD5.hexdigest(unique_key)[0..7]
  post.data['permalink'] = "/p/#{short_hash}/"
end

# 2. 注册 :pre_render 钩子双重保险
Jekyll::Hooks.register :posts, :pre_render do |post|
  unique_key = post.relative_path
  short_hash = Digest::MD5.hexdigest(unique_key)[0..7]
  post.data['permalink'] = "/p/#{short_hash}/"
end