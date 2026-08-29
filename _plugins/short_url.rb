require 'digest'

Jekyll::Hooks.register :posts, :pre_render do |post|
  # 如果文章 Front Matter 中没有手动指定 permalink
  unless post.data['permalink']
    # 提取文章的相对路径作为唯一基准（确保每篇文章算出来的 Hash 是固定且唯一的）
    unique_key = post.relative_path
    
    # 使用 MD5 计算哈希值，并截取前 8 位纯英数短字符
    short_hash = Digest::MD5.hexdigest(unique_key)[0..7]
    
    # 强制将该文章的 permalink 设为：/p/8位短字符/
    post.data['permalink'] = "/p/#{short_hash}/"
  end
end