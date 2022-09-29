# Shell Proxy

on_proxy () {
    export proxy="http://127.0.0.1:38457"
    export http_proxy=$proxy
    export https_proxy=$proxy
    export HTTP_PROXY=$proxy
    export HTTPS_PROXY=$proxy
}

off_proxy () {
    unset http_proxy
    unset https_proxy
    unset HTTP_PROXY
    unset HTTPS_PROXY
}