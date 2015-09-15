FROM centos:7

RUN yum -y install git rpmdevtools mock

RUN adduser centos
USER centos
ENV HOME /home/centos
WORKDIR /home/centos

RUN git clone https://github.com/tomhillable/consul-rpm.git consul-rpm
RUN rpmdev-setuptree
RUN ln -s $HOME/consul-rpm/SPECS/consul.spec $HOME/rpmbuild/SPECS/
RUN find $HOME/consul-rpm/SOURCES -type f -exec ln -s {} $HOME/rpmbuild/SOURCES/ \;

RUN spectool -g -R rpmbuild/SPECS/consul.spec
RUN rpmbuild -ba rpmbuild/SPECS/consul.spec

VOLUME /out
CMD find $HOME/rpmbuild -type d -name "RPMS" -exec cp -r {} /out/ \; && \
    find $HOME/rpmbuild -type d -name "SRPMS" -exec cp -r {} /out/ \;
