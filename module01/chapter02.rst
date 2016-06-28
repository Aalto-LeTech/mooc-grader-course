More exercise types
===================

This chapter presents two different exercise scenarios.

Submit a remote exercise
------------------------

This exercise opens an external tool via LTI launch protocol.
The LTI integration must be first configured at A+.

.. submit:: 3 50
  :url: https://rubyric.com/edge/exercises/111/lti
  :lti: Rubyric+
  :lti_context_id: asdasd
  :lti_resource_link_id: asdasd


Feedback questionnaire
----------------------

The questionnaire directive can also be used to collect student
input without grading it.

.. questionnaire::
  :feedback:

  What do you think now?

  .. freetext::
    :required:
    :length: 100
    :height: 4
    :class: my-input-class

  .. agree-group::

    .. agree-item:: Did it work for you?
