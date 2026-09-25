# Local LabAgent configuration

LabAgent skills and canonical protocols are Git-managed. Experiment records are not.

Each user or machine should provide a local configuration file outside the LabAgent repository at:

```text
~/.labagent/config.yaml
```

Minimum configuration:

```yaml
user: your-name

paths:
  labagent_repo: /absolute/path/to/LabAgent
  experiment_root: /absolute/path/to/experiment/storage
```

Additional machine- or user-specific paths may be added as needed, for example HPC project space, scratch directories, or mounted lab storage.

## Rules

- The local config must not be committed to LabAgent.
- `paths.labagent_repo` points to reusable Git-managed infrastructure.
- `paths.experiment_root` points to the external experiment store.
- Experiment lifecycle skills must never fall back to creating experiment records inside the LabAgent repository.
- Experiment records and experimental data must not be branched, committed, pushed, or otherwise synchronized through LabAgent Git.
- Reusable protocols, skills, templates, and other shared infrastructure may be maintained in LabAgent Git.
