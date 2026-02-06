# HR Cosigner

**Version:** 18.0.1.0.0  
**Category:** Human Resources  
**License:** LGPL-3  
**Author:** Custom Dev Team Top Tech

## Overview

The **HR Cosigner** module extends the standard Odoo Employee module to allow the management of cosigners (guarantors) for employees. It provides a structured way to store and track detailed information about individuals who sign as guarantors for employees, including their personal details, work information, financial status, and supporting documents.

## Features

*   **Cosigner Management:** Associate multiple cosigners with a single employee.
*   **Comprehensive Details:** Store detailed information for each cosigner:
    *   **Personal:** Photo, Full Name, Phone Number, Signing Date.
    *   **Living Address:** Country, State, City, Woreda, House Number.
    *   **Employment Information:** Employment Type (Private/Government), Job Title, Company Name, Company Address.
    *   **Financial Information:** Monthly Wage, Guaranteed Amount, Purpose of Guarantee.
*   **Document Attachments:** Upload and manage documents related to the cosigner (e.g., ID cards, signed forms) directly on the cosigner record.
*   **Employee Integration:**
    *   Adds a **Cosigners** smart button to the Employee form for quick access and count visibility.
    *   Adds a **Cosigners** tab within the Employee form to view and manage cosigners directly.
*   **Audit Tracking:** Changes to critical fields (Name, Phone, Address, Financials) are tracked in the chatter for audit purposes.

## Dependencies

*   `hr` (Employees)
*   `mail` (Discuss)

## Installation

1.  Place the `cosigners` module folder in your Odoo addons path.
2.  Restart the Odoo service.
3.  Go to **Apps**, search for "HR Cosigner", and click **Activate**.

## Usage

1.  Navigate to the **Employees** app.
2.  Open an **Employee** profile.
3.  You can manage cosigners in two ways:
    *   Click the **Cosigners** smart button at the top of the form.
    *   Scroll down to the **Cosigners** tab in the notebook.
4.  Click **Add a line** or **Create** to add a new cosigner.
5.  Fill in the required information:
    *   **Name** and **Phone** are mandatory.
    *   Upload a **Photo** if available.
    *   Fill in **Private Information** (Address).
    *   Fill in **Work Information** and **Financial Information**.
6.  Use the **Attachments** button or section to upload relevant files.
7.  Save the record.

## Technical Details

*   **Model:** `hr.cosigner`
*   **Inherits:** `mail.thread`, `mail.activity.mixin` (enables chatter and activities)
*   **Relation:** One-to-many relationship with `hr.employee` (`cosigner_ids`).
