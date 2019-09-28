from qiniu import Auth, put_file, etag
from swiper import cfg

def upload_to_qn(localfile, filename):
    # 需要填写你的 Access Key 和 Secret Key
    access_key = cfg.QN_ACCESSKEY
    secret_key = cfg.QN_SECRETKEY
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 上传后保存的文件名
    key = filename
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(cfg.QN_BUCKT, key, 3600)
    # 要上传文件的本地路径
    put_file(token, key, localfile)
    file_url = '/'.join([cfg.QN_BASEURL, filename])
    return  file_url


