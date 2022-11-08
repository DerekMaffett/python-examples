let
  pkgs = import <nixpkgs> {};
in
pkgs.mkShell {
  name="python-examples";
  buildInputs=[
  ];
}
