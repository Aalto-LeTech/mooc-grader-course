Introduction
============

This is study chapter sample that embeds two exercises
in the material. The idea is that the students study the subject
and solve exercises as they proceed in the material.

Multiple choice questionnaire
-----------------------------

The first exercise is a form where student answers and receives
feedback in the place.

.. questionnaire:: 1 7
  :submissions: 4
  :points-to-pass: 0

  This is a questionnaire number 1 that gives at maximum 7 points.
  Students can make at most 4 submissions. This exercise is marked
  passed when 0 points is reached (the default).

  .. pick-one:: 2

    Wait for the question in a code form:

    .. code-block:: none

      answer = 1 + 1

    a. 1
    *b. 2
    c. 3

    !b § Count again!
    c § Too much

  .. pick-any:: 2

    Which of the following are yellow?

    *a. banana
    *b. butter
    c. sea

    !a § All foods apply.
    !b § All foods apply.
    c § Sea is not a river.

  .. freetext:: string-ignorews

- title: 4. Type <kbd>blue</kbd> below.
  type: text
  points: 1
  correct: blue
  hint: Check exact spelling.

- title: 5. Type some <code>code</code> including word "<samp>test</samp>".
  type: text
  points: 1
  regex: .*test.*

A file submission exercise
--------------------------

    <p>
      In the second exercise, the student would receive information and
      instruction for writing a small computer program. Finally, the
      created program is submitted to this file form for grading.
    </p>
    <div data-aplus-exercise="2"></div>

    <p>
      Notice that in the last exercise the feedback is always in the
      dialog. This is good for exercises that receive much longer feedback
      than the original submission form.
    </p>




Graded questionnaire
--------------------

.. questionnaire:: 1 A50
  :submissions: 4
  :points-to-pass: 0

  This is a questionnaire number 1 that gives at maximum 50 points
  in category A. Students can make at most 4 submissions.
  This exercise is marked passed when 0 points is reached (the default).

  .. pick-one:: 10

    What is 1+1? The next block presents a program to calculate this.

    .. code-block:: none

      var value = 1 + 1

    a. 1
    *b. 2
    c. 3

    !b § Count again!
    c § Too much

  (Hints can be included or omitted in any question.)

  .. pick-any:: 10

    Pick two **first**.

    *a. this is **first**
    *b. this is **second**
    c. this is **third**

  .. freetext:: 30 string-ignorews-ignorequotes
    :length: 10

    A textual input can be compared with the model as int, float or string.
    Fourth option is regexp which takes the correct answer as a regular
    expression. Strings have comparison modifiers that are separated with hyphen.

    * ignorews: ignore white space (applies to regexp too)
    * ignorequotes: iqnore "quotes" around
    * requirecase: require identical lower and upper cases
    * ignorerepl: ignore REPL prefixes

    Here the correct answer is "test".

    test
    !test § Follow the instruction.


Feedback questionnaire
----------------------

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


Submit an exercise
------------------

These type of exercises are configured separately for mooc-grader.
The directive will attach the exercise at this position.

.. submit:: 2 A100
  :submissions: 100
  :config: exercises/hello_python/config.yaml


Submit a remote exercise
------------------------

This exercise opens an external tool via LTI launch protocol.

.. submit:: 3 B50
  :url: https://rubyric.com/edge/exercises/111/lti
  :lti: Rubyric+
  :lti_context_id: asdasd
  :lti_resource_link_id: asdasd
