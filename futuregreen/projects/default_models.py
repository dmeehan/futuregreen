# projects/default_models.py

"""

        Default models for the project app.
        Not loaded by syncdb unless specified in settings.
    
"""

from projects.models import ProjectBase, PhysicalProjectBase, PhysicalMixin

class Project(ProjectBase):
    """
        A non-abstract version of ProjectBase.
    """
    pass

class PhysicalProject(PhysicalProjectBase):
    """
       A non-abstract version of PhysicalProjectBase.
    """
    pass

class ProjectMulti(ProjectBase):
    """
       A non-abstract version of ProjectBase to be used
       for multi-table inheritance of projects.
    """
    pass

class PhysicalProjectMulti(ProjectMulti, PhysicalMixin):
    """
        Inherits from ProjectMulti via multi-table inheritance.
        Use this if you want to have both base projects and physical projects
        in your app and you want to be able to select all types
        as a single query.
    """
    pass