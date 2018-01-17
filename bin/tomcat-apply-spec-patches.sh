#!/bin/bash
# Script to apply patches in RPM specfile order
# Run from tomcat directory with src tar

# get sources if they don't exist
if ! [ -f apache-tomcat-*.tar.gz ]; then
    # fedpkg sources # if using fedora
    rhpkg sources
fi

# cleanup old dirs
if [ -d apache-tomcat-*-src ]; then
    rm -rf apache-tomcat-*-src
fi

# extract sources
tar xvf apache-tomcat-*.tar.gz > /dev/null

# spec package name
major=6
tomcat=tomcat${major}
minor=0

# cd into directory
pushd apache-tomcat*-src/
    for p in $(egrep Patch[0-9]+ ../${tomcat}.spec | awk '{print $2}' | sed -e "s/%{name}/${tomcat}/g" | sed -e "s/%{major_version}/${major}/g" | sed -e "s/%{minor_version}/${minor}/g"); do 
        echo "Applying $p..."
        patch -p0 < ../$p;
    done
popd
