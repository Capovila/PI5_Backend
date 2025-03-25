import express from "express";
import * as professoresController from "../controllers/profesoresController.js";

const router = express.Router();

router.get("/", professoresController.getProfessores);
router.get("/:id", professoresController.getProfessoresById);

export default router;
