Feature: Student Gradebook Application

  Scenario: AC-1-001: User can add student with valid numeric grade
    Given I am on the gradebook application
    When I enter "John Doe" in the name field
    And I enter "Math" in the subject field
    And I enter "85" in the grade field
    And I click the Add button
    Then the student "John Doe - Math - 85" should be displayed in the student list

  Scenario: AC-1-002: User can add multiple students with different subjects
    Given I am on the gradebook application
    When I enter "Jane Smith" in the name field
    And I enter "English" in the subject field
    And I enter "90" in the grade field
    And I click the Add button
    And I enter "Bob Wilson" in the name field
    And I enter "Science" in the subject field
    And I enter "75" in the grade field
    And I click the Add button
    Then the student "Jane Smith - English - 90" should be displayed in the student list
    And the student "Bob Wilson - Science - 75" should be displayed in the student list

  Scenario: AC-2-001: Display error for non-numeric grade input
    Given I am on the gradebook application
    When I enter "Alice Brown" in the name field
    And I enter "Physics" in the subject field
    And I enter "ABC" in the grade field
    And I click the Add button
    Then an error message should be displayed indicating invalid grade

  Scenario: AC-2-002: Handle empty grade field
    Given I am on the gradebook application
    When I enter "Charlie Davis" in the name field
    And I enter "History" in the subject field
    And I leave the grade field empty
    And I click the Add button
    Then an error message should be displayed or the student should not be added
