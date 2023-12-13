# Use the official Odoo image as a parent image
FROM odoo:14.0

# Switch to the root user to install additional packages
# USER root

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools


# Install pandas using pip
RUN pip3 install pandas requests

# Switch back to the Odoo user
# USER odoo
