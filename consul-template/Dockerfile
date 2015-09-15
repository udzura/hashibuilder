FROM centos:7

RUN yum -y install git rpmdevtools mock

RUN adduser centos
USER centos
ENV HOME /home/centos
WORKDIR /home/centos

ADD consul-template-rpm /home/centos/consul-template-rpm
RUN rpmdev-setuptree
RUN ln -s $HOME/consul-template-rpm/SPECS/consul-template.spec $HOME/rpmbuild/SPECS/
RUN find $HOME/consul-template-rpm/SOURCES -type f -exec ln -s {} $HOME/rpmbuild/SOURCES/ \;

RUN spectool -g -R rpmbuild/SPECS/consul-template.spec
RUN rpmbuild -ba rpmbuild/SPECS/consul-template.spec

VOLUME /out
CMD find $HOME/rpmbuild -type d -name "RPMS" -exec cp -r {} /out/ \; && \
    find $HOME/rpmbuild -type d -name "SRPMS" -exec cp -r {} /out/ \;
