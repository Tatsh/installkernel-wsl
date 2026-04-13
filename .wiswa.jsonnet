local utils = import 'utils.libjsonnet';

{
  uses_user_defaults: true,
  description: 'Script and installkernel hook to copy Linux kernel to the host system and update .wslconfig.',
  keywords: ['command line', 'wsl'],
  project_name: 'installkernel-wsl',
  version: '0.0.4',
  want_main: true,
  want_flatpak: false,
  want_snap: false,
  supported_platforms: ['linux'],
}
