def list_candidates(tag_name, limit=None):
    def wrap(func):
        def wrapped_func(*args, **kwargs):
            user = args[0].user
            query_params = func(*args, **kwargs)
            if limit is not None:
                query_params["limit"] = 1000
                query_params["offset"] = 3100
            user.client.get(
                "/candidates",
                headers=user.get_auth_headers(),
                params=query_params,
                name="/candidates:{}".format(tag_name),
            )

        return wrapped_func

    return wrap
