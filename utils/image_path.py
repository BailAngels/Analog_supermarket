def upload_avatar_for_user(instance, filename):
    return f"/avatar/{instance.username}/{filename}"


def upload_product(instance, filename):
    return f"/product/{instance.product.title}/{filename}"
