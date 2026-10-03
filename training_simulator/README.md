# Training Simulator 🎓

A **beginner-friendly** leaver detection simulator for learning insider threat detection concepts before diving into the full multi-agent system.

## 🎯 Purpose

This training module provides a simplified introduction to:
- Behavioral pattern analysis
- Risk scoring fundamentals
- Basic AI agent concepts
- Statistical anomaly detection

**Start here**, then progress to the advanced multi-agent system in the parent directory.

## 🆚 Training vs. Full System

| Feature | Training Simulator | Full System (Parent) |
|---------|-------------------|---------------------|
| **Purpose** | Educational | Production-ready |
| **Complexity** | Beginner-friendly | Enterprise-grade |
| **Agents** | Single rule-based | Multi-agent orchestration |
| **Data Sources** | Simple CSV | GCP telemetry simulation |
| **LLM Integration** | Optional | LangGraph + Claude API |
| **MITRE Mapping** | None | Full ATT&CK integration |
| **Setup Time** | 5 minutes | 30+ minutes |

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- No API keys needed!

### Run the Simulator

```bash
# Navigate to training simulator
cd training_simulator

# Run example
cd examples
python run_simulation.py
```

### 🤖 Using with Claude Code

If you're using Claude Code CLI and want to skip permission prompts:

```bash
# Option 1: Bypass permissions (use cautiously)
claude --dangerously-skip-permissions

# Option 2: Permission mode bypass
claude --permission-mode bypassPermissions
```

**Note**: These flags skip permission prompts for file operations. Only use in trusted development environments.

### Output
```
Leaver Detection Simulator - Example Run
============================================================
[1/4] Generating synthetic user behavior data...
      Generated 14882 activities for 25 users

[2/4] Running statistical detection analysis...
      Detected 5 potential leavers

[3/4] Running AI agent analysis...
      Completed AI analysis for 5 users

[4/4] Generating final report...
      Report saved to: ../data/detection_report.txt
============================================================
```

## 📁 Files

```
training_simulator/
├── src/
│   ├── data_generator.py     # Create synthetic user data
│   ├── detector.py           # Statistical detection
│   ├── agent.py              # Simple AI agent
│   └── simulator.py          # Main orchestrator
├── examples/
│   └── run_simulation.py     # Run a demo
├── tests/
│   └── test_detector.py      # Unit tests
└── data/                      # Generated outputs
```

## 🎓 Learning Path

### 1. **Start Here** (Training Simulator)
   - Understand basic concepts
   - Learn data generation
   - Explore simple detection logic
   - Run your first simulation

### 2. **Progress To** (Main System)
   - Multi-agent architecture
   - Real GCP telemetry patterns
   - LLM-powered analysis
   - MITRE ATT&CK mapping

## 🔧 How It Works

### Data Generation
Creates synthetic user behavior:
- **Normal users**: 9-5 activity, low risk
- **Leavers**: After-hours access, data exports, external emails

### Detection
Statistical risk scoring based on:
- Activity frequency
- Time patterns
- Data movement
- Communication changes

### AI Agent
Rule-based pattern matching for:
- Data hoarding
- Unusual timing
- Communication changes
- Access expansion

## 📊 Customize the Simulation

Edit `examples/run_simulation.py`:

```python
results = simulator.run_full_simulation(
    num_normal=50,    # More users
    num_leavers=10    # More leavers
)
```

Adjust risk threshold in `src/simulator.py`:

```python
self.detector = LeaverDetector(risk_threshold=0.7)
```

## 🧪 Run Tests

```bash
cd tests
python test_detector.py
```

## 📚 Next Steps

After completing the training simulator:

1. **Review the main system**: `cd .. && cat README.md`
2. **Explore the architecture**: Check `ARCHITECTURE.md`
3. **Set up the full system**: Follow `GETTING_STARTED.md`
4. **Try the live dashboard**: `streamlit run dashboard/app.py`

## 💡 Key Differences From Main System

| Concept | Training | Production |
|---------|----------|------------|
| Data | Synthetic CSV | GCP API simulation |
| Detection | Statistical rules | ML + LLM hybrid |
| Agents | 1 rule-based | 5+ specialized agents |
| Speed | Immediate | Parallel execution |
| Output | Text report | Interactive dashboard |
| Integration | Standalone | SOAR/SIEM ready |

## 🤝 Contributing

Found a bug or have an improvement? 
- Training module issues: Tag with `training-simulator`
- Main system issues: Use standard labels

## 📝 License

MIT License (same as parent project)

---

**Ready for the full system?** Head back to the main directory:
```bash
cd ..
cat GETTING_STARTED.md
```
