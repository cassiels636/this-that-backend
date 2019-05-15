with import <nixpkgs> {};
stdenv.mkDerivation rec {
    name = "env";
    env = buildEnv { name = name; paths = buildInputs; };
    builder = builtins.toFile "builder.sh" ''
        source $stdenv/setup; ln -s $env $out
    '';

    buildInputs = [
        (python35.buildEnv.override {
            ignoreCollisions = true;
            extraLibs = with python36Packages; [
                django_2_1
                djangorestframework
                pytz
            ];
        })
    ];
}