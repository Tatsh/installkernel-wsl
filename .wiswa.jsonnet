local utils = import 'utils.libjsonnet';

(import 'defaults.libjsonnet') + {
  // Project-specific
  description: 'Script and installkernel hook to copy Linux kernel to the host system and update .wslconfig.',
  keywords: ["command line", "wsl"],
  project_name: 'installkernel-wsl',
  version: '0.0.1',
  want_main: true,
  citation+: {
    'date-released': '2025-04-12',
  },
  pyproject+: {
    tool+: {
      poetry+: {
        dependencies+: {
          click: '^8.1.8',
        },
      },
    },
  },
  // Common
  authors: [
    {
      'family-names': 'Udvare',
      'given-names': 'Andrew',
      email: 'audvare@gmail.com',
      name: '%s %s' % [self['given-names'], self['family-names']],
    },
  ],
  local funding_name = '%s2' % std.asciiLower(self.github_username),
  github_username: 'Tatsh',
  github+: {
    funding+: {
      ko_fi: funding_name,
      liberapay: funding_name,
      patreon: funding_name,
    },
  },
}
