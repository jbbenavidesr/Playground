# Personal Coding Playground

## Purpose

This repository is my personal space for:

- Learning and experimenting with new technologies
- Storing small projects and code snippets
- Tracking my coding journey and skill development

## Repository Structure

### Projects

Each project is located in the `projects/` directory with a unique numerical identifier.

#### Project Organization

- Numbered sequentially (001, 002, etc.)
- Includes a `.tags` file for metadata and categorization
- Contains source code, README, and related files

### Tagging System

Projects are tagged using a simple YAML-based system in the `.tags` file:

- Easy to read and modify manually
- Supports multiple tags and metadata
- Helps in project discovery and tracking

#### `.tags` template

```yaml
identifier: 001
name: <project_name>
description: <project_description>

tags:
  - language: <programming_language> # Could also be a list
  - domain:
      # List of domains explored in the project (some examples)
      - web development
      - performance
  - tools:
      # Tools to be used
      - flexbox
      - django
  - difficulty: <difficulty>
  - status: <current_status>

metadata:
  created: <creation_date>
  last-updated: <update_date>
  learning-goals:
    # Learning goals of the project
    - Practice web development with django
    - Learn django performance techniques

links:
  # Link for important resources like course, book or tutorial followed.
  - <link_name>: <url>

notes:
  - Some notes for when I come back or for remembering my steps
```

## How to Use This Repository

### Starting a New Project

1. Create a new directory in `projects/` with the next sequential number
2. Add a `.tags` file describing the project
3. Include a README and your project files

### Finding Projects

- Browse the `projects/` directory
- Check `.tags` files for project details
- Use text search or manual filtering

## Guidelines

- Keep projects small and focused
- Document your learning process
- Update `.tags` file as project evolves
- Move significant projects to dedicated repositories

## Current Project Areas of Interest

- Software Architecture
- Test Driven Development
- Domain Driven Design
- Development of project templates and boilerplates
- Python Programming
- Web Development

## Contact

Feel free to reach out if you're interested in my learning journey or have suggestions!

_This is a personal playground - expect experiments, mistakes, and continuous learning._
