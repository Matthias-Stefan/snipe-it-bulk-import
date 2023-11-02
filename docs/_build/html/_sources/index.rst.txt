Welcome to Snipe-IT Bulk Import's documentation!
================================================

.. automodule:: main
    :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Contents
========

.. toctree::
   :maxdepth: 2
   :caption: Controller

   src/controller/checkout_controller
   src/controller/create_asset_controller
   src/controller/interface_controller
   src/controller/main_controller
   src/controller/settings_controller
   src/controller/upload_controller

.. toctree::
   :maxdepth: 2
   :caption: Execution

   src/execution/checkout_upload_executor
   src/execution/interface_execution
   src/execution/model_upload_executor
   src/execution/upload_executor

.. toctree::
   :maxdepth: 2
   :caption: Manager

   src/manager/endpoint
   src/manager/logger
   src/manager/snipe_manager

.. toctree::
   :maxdepth: 2
   :caption: Model

   src/model/asset
   src/model/checkout
   src/model/create_asset
   src/model/field
   src/model/interface_model
   src/model/settings
   src/model/upload

.. toctree::
   :maxdepth: 2
   :caption: Template

   src/template/create_asset_template
   src/template/create_checkout_template
   src/template/interface_template

.. toctree::
   :maxdepth: 2
   :caption: User Interface Components

   src/view/checkout_tab
   src/view/create_asset_tab
   src/view/file_browser
   src/view/main_view
   src/view/progress
   src/view/settings_tab
   src/view/upload_tab

.. toctree::
   :maxdepth: 2
   :caption: Utility

   src/utility/events
   src/utility/exceptions
   src/utility/profiling
   src/utility/singleton
