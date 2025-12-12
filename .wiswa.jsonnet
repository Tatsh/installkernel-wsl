local utils = import 'utils.libjsonnet';

{
  description: 'Script and installkernel hook to copy Linux kernel to the host system and update .wslconfig.',
  keywords: ['command line', 'wsl'],
  project_name: 'installkernel-wsl',
  version: '0.0.4',
  want_main: true,
  copilot: {
    intro: 'installkernel-wsl is a script and installkernel hook to copy Linux kernel to the host system and update `.wslconfig.`',
  },
}
