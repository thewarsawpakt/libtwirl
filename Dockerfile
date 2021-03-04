FROM	archlinux:base-devel

WORKDIR	/usr/local/src

RUN	pacman -Syu --noconfirm git python pyalpm && \
	git clone https://github.com/Generic-Linux/libtwirl && \
    cd libtwirl && python3 -m libtwirl install bash
