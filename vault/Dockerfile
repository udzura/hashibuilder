FROM centos:7

RUN yum -y install git rpmdevtools mock

RUN adduser centos
USER centos
ENV HOME /home/centos
WORKDIR /home/centos

RUN git clone https://github.com/udzura/vault-rpm.git vault-rpm
RUN rpmdev-setuptree
RUN ln -s $HOME/vault-rpm/SPECS/vault.spec $HOME/rpmbuild/SPECS/
RUN find $HOME/vault-rpm/SOURCES -type f -exec ln -s {} $HOME/rpmbuild/SOURCES/ \;

RUN spectool -g -R rpmbuild/SPECS/vault.spec
RUN rpmbuild -ba rpmbuild/SPECS/vault.spec

VOLUME /out
CMD find $HOME/rpmbuild -type d -name "RPMS" -exec cp -r {} /out/ \; && \
    find $HOME/rpmbuild -type d -name "SRPMS" -exec cp -r {} /out/ \;
