installkernel_wsl
=================

Script and installkernel hook to copy Linux kernel to the host system and update .wslconfig.

Commands
--------

.. click:: installkernel_wsl.main:main
  :prog: installkernel-wsl
  :nested: full

Usage as a hook
---------------

After installation:

.. code-block:: bash

   mkdir -p /etc/kernel/install.d
   ln -sf "$(command -v installkernel-wsl)" /etc/kernel/install.d/99-wsl-kernel.install

.. only:: html

   Library
   -------
   .. automodule:: installkernel_wsl.utils
      :members:

   Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
